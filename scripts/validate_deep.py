#!/usr/bin/env python3
"""深度验证：检查工作流在 n8n 中能否正常导入和运行。

检查项: JSON合法性 | 连接有效性 | 必需参数 | 孤立节点

用法: python scripts/validate_deep.py
"""

import json, glob, os, sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF_DIR = os.path.join(BASE, "workflows")

REQUIRED_PARAMS = {
    'n8n-nodes-base.httpRequest': ['url', 'method'],
    'n8n-nodes-base.emailSend': ['fromEmail', 'toEmail', 'subject'],
    '@n8n/n8n-nodes-langchain.lmChatOpenAi': ['model'],
    '@n8n/n8n-nodes-langchain.agent': ['agent'],
    'n8n-nodes-base.code': ['jsCode'],
    'n8n-nodes-base.if': ['conditions'],
    'n8n-nodes-base.switch': ['rules'],
}


def get_targets(conn_data):
    """从 n8n 嵌套连接结构中提取所有目标节点名"""
    names = set()
    if not isinstance(conn_data, dict):
        return names
    for output, items in conn_data.items():
        if isinstance(items, list):
            for item in items:
                if isinstance(item, list):
                    for conn in item:
                        if isinstance(conn, dict) and conn.get('node'):
                            names.add(conn['node'])
                elif isinstance(item, dict) and item.get('node'):
                    names.add(item['node'])
    return names


def validate_one(wf_path):
    cat = os.path.basename(os.path.dirname(os.path.dirname(wf_path)))
    name = os.path.basename(os.path.dirname(wf_path))
    label = f"{cat}/{name}"
    issues = []

    try:
        with open(wf_path, encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [('error', 'json', str(e))]

    nodes = data.get('nodes', [])
    conns = data.get('connections', {})
    
    node_names = {n.get('name') for n in nodes if n.get('name')}
    sticky = {'n8n-nodes-base.stickyNote'}
    real_names = {n.get('name') for n in nodes if n.get('type','') not in sticky}

    # Check: connection source exists
    for src in conns:
        if src not in node_names:
            issues.append(('error', 'bad_src', f"源 '{src}' 不存在"))
    
    # Check: connection target exists
    for src in conns:
        for tgt in get_targets(conns[src]):
            if tgt not in node_names:
                issues.append(('error', 'bad_tgt', f"'{src}'→'{tgt}' 目标不存在"))

    # Check: connected nodes coverage
    connected = set()
    for src in conns:
        connected.add(src)
        for t in get_targets(conns[src]):
            connected.add(t)
    for n in real_names:
        if n not in connected:
            issues.append(('warning', 'orphan', f"节点 '{n}' 无连接"))

    # Check: required params
    for n in nodes:
        ntype = n.get('type', '')
        if ntype in sticky:
            continue
        params = n.get('parameters', {}) or {}
        for p in REQUIRED_PARAMS.get(ntype, []):
            v = params.get(p)
            if v is None or v == '' or (isinstance(v, dict) and not v):
                issues.append(('warning', 'missing_param', f"'{n.get('name','?')}' 缺 {p}"))

    if not issues:
        issues.append(('ok', 'ok', ''))
    return [(s, t, f'{label}: {d}') for s, t, d in issues]


def main():
    all_r = []
    for wf in sorted(glob.glob(os.path.join(BASE, 'workflows/*/*/workflow.json'))):
        all_r.extend(validate_one(wf))

    ok = sum(1 for s,_,_ in all_r if s == 'ok')
    errs = [(s,t,d) for s,t,d in all_r if s == 'error']
    warns = [(s,t,d) for s,t,d in all_r if s == 'warning']

    print(f"\n{'='*60}")
    print(f"  深度验证: {len(all_r)//6} 工作流")
    print(f"  ✅ 通过: {ok}  |  ❌ 错误: {len(errs)}  |  ⚠️ 警告: {len(warns)}")
    print(f"{'='*60}\n")

    if errs:
        print(f"❌ 结构错误 ({len(errs)}):")
        for _, t, d in errs[:15]:
            print(f"  [{t}] {d}")
        if len(errs) > 15:
            print(f"  ... 及 {len(errs)-15} 条")
        print()

    if warns:
        wc = Counter(t for _, t, _ in warns)
        print(f"⚠️  警告分布:")
        for t, c in wc.most_common():
            print(f"  {t}: {c}")

    return 0 if not errs else 1


if __name__ == '__main__':
    sys.exit(main())
