#!/usr/bin/env python3
"""切换工作流的国内/海外节点配置。

每个被替换的节点在 _cn_meta.replacements 中保存了原始配置。
切换时：
  国内模式(cn)：    使用飞书/阿里云/通义万相等国内方案
  海外模式(overseas)：恢复原始 Slack/Gmail/Google 等节点

用法:
  python scripts/toggle_region.py cn        # 切换到国内方案（默认）
  python scripts/toggle_region.py overseas  # 切换回海外原始节点
  python scripts/toggle_region.py status    # 查看当前分布
"""

import json, glob, sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/你的飞书机器人Webhook地址"

# CN replacement params for each overseas type
def _cn_params(overseas_type, label):
    t = overseas_type.replace('n8n-nodes-base.', '')
    
    if t in ('slack', 'discord'):
        return {
            'url': FEISHU_WEBHOOK, 'method': 'POST', 'sendBody': True,
            'bodyParameters': {'parameters': [{'name': 'body', 'value': json.dumps({"msg_type":"interactive","card":{"header":{"title":{"tag":"plain_text","content":"n8n 通知"}},"elements":[{"tag":"markdown","content":"消息内容"}]}}, ensure_ascii=False)}]},
            'options': {}, 'notes': f'原 {label}。切换: scripts/toggle_region.py overseas'
        }
    if t == 'googleDrive':
        return {
            'url': 'https://oss-cn-hangzhou.aliyuncs.com/你的Bucket/文件路径', 'method': 'PUT',
            'options': {}, 'notes': f'原 {label}。切换: scripts/toggle_region.py overseas'
        }
    # Default: Feishu Bitable for sheets/airtable/calendar/notion/hubspot
    return {
        'url': 'https://open.feishu.cn/open-apis/bitable/v1/apps/你的AppToken/tables/你的表格ID/records',
        'method': 'GET', 'sendHeaders': True,
        'headerParameters': {'parameters': [{'name': 'Authorization', 'value': 'Bearer 你的飞书应用Token'}]},
        'options': {}, 'notes': f'原 {label}。切换: scripts/toggle_region.py overseas'
    }


def toggle(target):
    count = 0
    for wf_path in glob.glob(os.path.join(BASE, 'workflows/*/*/workflow.json')):
        with open(wf_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        replacements = data.get('_cn_meta', {}).get('replacements', {})
        if not replacements:
            continue

        nodes = data.get('nodes', [])
        modified = False

        for n in nodes:
            nid = n.get('id', '')
            if nid not in replacements:
                continue
            orig = replacements[nid]

            if target == 'overseas':
                # 恢复海外原始节点
                n['type'] = orig['type']
                n['parameters'] = orig['parameters']
                if 'typeVersion' in orig:
                    n['typeVersion'] = orig['typeVersion']
                modified = True
            else:
                # 应用国内替换
                if n.get('type') == orig['type']:
                    # 当前是海外模式，切换为国内
                    n['type'] = 'n8n-nodes-base.httpRequest'
                    n['parameters'] = _cn_params(orig['type'], orig['type'].replace('n8n-nodes-base.', ''))
                    if 'typeVersion' in n:
                        del n['typeVersion']
                    modified = True

        if modified:
            data['_cn_meta']['region'] = target
            with open(wf_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            count += 1
    return count


def status():
    cn = ov = 0
    for wf_path in glob.glob(os.path.join(BASE, 'workflows/*/*/workflow.json')):
        with open(wf_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data.get('_cn_meta', {}).get('replacements'):
            r = data['_cn_meta'].get('region', 'cn')
            if r == 'cn': cn += 1
            else: ov += 1
    print(f'含替换的流程: {cn + ov}')
    print(f'  国内模式: {cn}')
    print(f'  海外模式: {ov}')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'cn':
        print(f'已切换 {toggle("cn")} 个流程 → 国内方案')
    elif cmd == 'overseas':
        print(f'已切换 {toggle("overseas")} 个流程 → 海外原始节点')
    else:
        status()
