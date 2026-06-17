#!/usr/bin/env python3
"""Generate docs/ site with searchable workflow browser."""

import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF_DIR = os.path.join(BASE, "workflows")
DOCS_DIR = os.path.join(BASE, "docs")

CATEGORY_NAMES = {
    "ai-agent": "AI Agent",
    "devops": "DevOps",
    "finance-analysis": "Finance Analysis",
    "knowledge-rag": "Knowledge RAG",
    "multimodal-ai": "Multimodal AI",
    "workflow-automation": "Workflow Automation",
}

CATEGORY_ICONS = {
    "ai-agent": "",
    "devops": "",
    "finance-analysis": "",
    "knowledge-rag": "",
    "multimodal-ai": "",
    "workflow-automation": "",
}

# Reuse the classification rules from build_index.py
def get_classification_rules():
    from build_index import RULES
    return RULES

RULES = None

def load_rules():
    global RULES
    import sys
    sys.path.insert(0, os.path.join(BASE, "scripts"))
    from build_index import RULES as r
    RULES = r

def classify(category, name_lower):
    rules = RULES.get(category, [("其他", None, lambda n: True)])
    for sub_name, _, fn in rules:
        if fn(name_lower):
            return sub_name
    return "其他"

def make_tags(name_lower):
    """Extract relevant tags from workflow name."""
    pairs = {
        "chatbot": "聊天机器人",
        "chat": "对话",
        "agent": "Agent",
        "mcp": "MCP",
        "rag": "RAG",
        "telegram": "Telegram",
        "whatsapp": "WhatsApp",
        "slack": "Slack",
        "email": "邮件",
        "gmail": "Gmail",
        "api": "API",
        "webhook": "Webhook",
        "backup": "备份",
        "deploy": "部署",
        "docker": "Docker",
        "kubernetes": "K8s",
        "monitor": "监控",
        "alert": "告警",
        "stock": "股票",
        "crypto": "加密货币",
        "forex": "外汇",
        "vector": "向量",
        "qdrant": "Qdrant",
        "pinecone": "Pinecone",
        "image": "图片",
        "video": "视频",
        "voice": "语音",
        "audio": "音频",
        "scrape": "采集",
        "crawl": "爬虫",
        "form": "表单",
        "invoice": "发票",
        "payment": "支付",
        "seo": "SEO",
        "blog": "博客",
        "social": "社交媒体",
        "job": "求职",
        "hr": "HR",
        "lead": "线索",
        "crm": "CRM",
        "ticket": "工单",
        "weather": "天气",
        "news": "新闻",
        "pdf": "PDF",
        "database": "数据库",
        "postgresql": "PostgreSQL",
        "mysql": "MySQL",
        "server": "服务器",
        "linux": "Linux",
        "n8n": "n8n",
        "oauth": "OAuth",
        "ssh": "SSH",
        "transcribe": "转录",
        "tts": "TTS",
        "search": "搜索",
        "summary": "摘要",
        "translate": "翻译",
        "calendar": "日历",
        "schedule": "排程",
        "booking": "预约",
        "notion": "Notion",
    }
    tags = []
    for key, cn in pairs.items():
        if key in name_lower:
            tags.append(cn)
    return tags[:5]


def generate_data():
    load_rules()
    workflows = []
    for cat in sorted(os.listdir(WF_DIR)):
        cat_path = os.path.join(WF_DIR, cat)
        if not os.path.isdir(cat_path) or cat.startswith("."):
            continue
        if cat not in CATEGORY_NAMES:
            continue
        for wf_dir in sorted(os.listdir(cat_path)):
            wf_path = os.path.join(cat_path, wf_dir)
            if not os.path.isdir(wf_path):
                continue
            name_lower = wf_dir.lower()
            sub = classify(cat, name_lower)
            tags = make_tags(name_lower)

            # Read tier from _cn_meta
            tier = "B"
            wf_json = os.path.join(wf_path, "workflow.json")
            if os.path.exists(wf_json):
                try:
                    with open(wf_json, "r", encoding="utf-8") as f:
                        meta = json.load(f).get("_cn_meta", {})
                        tier = meta.get("tier", "B")
                except Exception:
                    pass

            # Read description_zh
            desc = ""
            if os.path.exists(wf_json):
                try:
                    with open(wf_json, "r", encoding="utf-8") as f:
                        meta = json.load(f).get("_cn_meta", {})
                        desc = meta.get("description_zh", "")
                except Exception:
                    pass

            # Detect required APIs
            api_needs = []
            all_nodes_text = ''
            if os.path.exists(wf_json):
                try:
                    with open(wf_json, "r", encoding="utf-8") as f:
                        nodes_data = json.load(f).get("nodes", [])
                    all_types = ' '.join(n.get('type','') for n in nodes_data)
                    if 'telegram' in all_types: api_needs.append('Telegram')
                    if any(t in all_types for t in ['lmChat','openAi','langchain','agent']): api_needs.append('DeepSeek')
                    if any(t in all_types for t in ['email','mail']): api_needs.append('邮箱')
                    if 'postgres' in all_types: api_needs.append('PostgreSQL')
                    if 'redis' in all_types: api_needs.append('Redis')
                    if 'serp' in all_types or 'search' in all_types.lower(): api_needs.append('搜索API')
                except Exception:
                    pass

            workflows.append({
                "name": wf_dir,
                "category": cat,
                "categoryName": CATEGORY_NAMES.get(cat, cat),
                "categoryIcon": CATEGORY_ICONS.get(cat, ""),
                "subcategory": sub,
                "tags": tags,
                "tier": tier,
                "desc": desc,
                "apiNeeds": api_needs,
                "path": f"https://github.com/LuckTerence/n8n-workflows-cn/tree/main/workflows/{cat}/{wf_dir}/",
                "readme": f"https://github.com/LuckTerence/n8n-workflows-cn/blob/main/workflows/{cat}/{wf_dir}/readme.md",
            })
    return workflows


def generate_html():
    workflows = generate_data()
    
    # Write data file
    os.makedirs(DOCS_DIR, exist_ok=True)
    data_path = os.path.join(DOCS_DIR, "workflows.json")
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(workflows, f, ensure_ascii=False)
    
    # Collect categories and subcategories for nav
    cats = {}
    for w in workflows:
        c = w["category"]
        if c not in cats:
            cats[c] = {"name": w["categoryName"], "icon": w["categoryIcon"], "subs": {}}
        sub = w["subcategory"]
        if sub not in cats[c]["subs"]:
            cats[c]["subs"][sub] = 0
        cats[c]["subs"][sub] += 1
    
    cat_order = ["ai-agent", "devops", "finance-analysis", "knowledge-rag", "multimodal-ai", "workflow-automation"]
    ordered_cats = [(c, cats[c]) for c in cat_order if c in cats]
    
    # Build nav HTML
    nav_html = ""
    for cid, cdata in ordered_cats:
        total = sum(cdata["subs"].values())
        nav_html += f'<div class="cat-group">\n'
        nav_html += f'  <div class="cat-header" onclick="toggleCat(this)">{cdata["icon"]} {cdata["name"]} <span class="count">({total})</span></div>\n'
        nav_html += f'  <div class="cat-body">\n'
        for sub_name, count in sorted(cdata["subs"].items()):
            nav_html += f'    <a href="#!" class="sub-link" data-cat="{cid}" data-sub="{sub_name}" onclick="filterSub(\'{cid}\', \'{sub_name}\'); return false;">{sub_name} <span>{count}</span></a>\n'
        nav_html += f'  </div>\n'
        nav_html += f'</div>\n'
    
    # Read template
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>n8n-workflows-cn — 工作流模板浏览器</title>
<style>
:root {{
    --bg: #0f0f11;
    --card: #1a1a1f;
    --border: #2a2a30;
    --text: #e0e0e0;
    --muted: #888;
    --accent: #4caf50;
    --accent2: #2196f3;
    --tag-bg: #252530;
    --hover: #222228;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }}

/* Sidebar */
.sidebar {{
    width: 260px; min-width: 260px; background: var(--card); border-right: 1px solid var(--border);
    display: flex; flex-direction: column; overflow: hidden;
}}
.sidebar-header {{
    padding: 20px 16px 12px; border-bottom: 1px solid var(--border);
}}
.sidebar-header h1 {{ font-size: 18px; font-weight: 700; margin-bottom: 4px; }}
.sidebar-header a {{ color: var(--muted); font-size: 13px; text-decoration: none; }}
.sidebar-header a:hover {{ color: var(--accent2); }}
.sidebar-nav {{ flex: 1; overflow-y: auto; padding: 8px; }}
.cat-group {{ margin-bottom: 4px; }}
.cat-header {{
    padding: 8px 10px; font-size: 14px; font-weight: 600; color: var(--text);
    cursor: pointer; border-radius: 6px; display: flex; align-items: center; gap: 6px;
    user-select: none;
}}
.cat-header:hover {{ background: var(--hover); }}
.cat-header .count {{ color: var(--muted); font-weight: 400; font-size: 12px; }}
.cat-body {{ display: block; }}
.cat-body.collapsed {{ display: none; }}
.sub-link {{
    display: flex; justify-content: space-between; align-items: center;
    padding: 5px 10px 5px 28px; font-size: 13px; color: var(--muted);
    text-decoration: none; border-radius: 4px; transition: background .15s;
}}
.sub-link:hover {{ background: var(--hover); color: var(--text); }}
.sub-link.active {{ background: var(--tag-bg); color: var(--accent); font-weight: 500; }}
.sub-link span {{ font-size: 11px; color: var(--muted); }}

/* Main */
.main {{ flex: 1; display: flex; flex-direction: column; overflow: hidden; }}
.toolbar {{
    padding: 12px 20px; background: var(--card); border-bottom: 1px solid var(--border);
    display: flex; gap: 12px; align-items: center; flex-wrap: wrap;
}}
.search-box {{
    flex: 1; min-width: 240px; padding: 10px 16px;
    background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
    color: var(--text); font-size: 14px; outline: none;
}}
.search-box:focus {{ border-color: var(--accent2); }}
.badge {{
    background: var(--tag-bg); color: var(--muted); padding: 6px 12px;
    border-radius: 20px; font-size: 13px; cursor: pointer; border: none;
    white-space: nowrap; transition: all .15s;
}}
.badge:hover {{ color: var(--text); }}
.badge.active {{ background: var(--accent); color: #fff; }}
#clear-btn {{ color: #e57373; cursor: pointer; font-size: 13px; display: none; }}
.results-info {{ padding: 10px 20px; color: var(--muted); font-size: 13px; border-bottom: 1px solid var(--border); }}
.list {{ flex: 1; overflow-y: auto; padding: 12px 20px; }}
.card {{
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px 18px; margin-bottom: 8px; transition: background .15s;
}}
.card:hover {{ background: var(--hover); }}
.card-title {{
    font-size: 15px; font-weight: 600; margin-bottom: 6px; line-height: 1.4;
}}
.card-title a {{ color: var(--text); text-decoration: none; }}
.card-title a:hover {{ color: var(--accent2); }}
.card-meta {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }}
.tag {{
    background: var(--tag-bg); color: var(--muted); padding: 2px 8px;
    border-radius: 4px; font-size: 12px;
}}
.cat-tag {{ color: var(--accent); }}
.sub-tag {{ color: var(--accent2); }}

/* Responsive */
@media (max-width: 768px) {{
    .sidebar {{ display: none; }}
}}
.github-corner {{ position: absolute; top: 0; right: 0; }}
.scenario-guide {{
    padding: 16px 20px; border-bottom: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(33,150,243,0.06) 0%, transparent 100%);
    display: none;
}}
.scenario-guide.visible {{ display: block; }}
.scenario-guide h3 {{ font-size: 14px; font-weight: 600; margin-bottom: 10px; color: var(--accent2); }}
.scenario-list {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.scenario-chip {{
    padding: 6px 14px; background: var(--tag-bg); border: 1px solid var(--border);
    border-radius: 8px; font-size: 13px; color: var(--text); cursor: pointer;
    transition: all .15s; text-decoration: none; white-space: nowrap;
}}
.scenario-chip:hover {{ background: var(--accent2); color: #fff; border-color: var(--accent2); }}
.tier-a {{ color: #4caf50; font-weight: 600; }}
.tier-b {{ color: #ff9800; font-weight: 600; }}
.card-desc {{ font-size: 12px; color: var(--muted); margin-top: 4px; line-height: 1.5; }}
.card-apis {{ margin-top: 4px; }}
.api-tag {{ font-size: 11px; color: var(--accent); background: rgba(76,175,80,0.1); padding: 1px 6px; border-radius: 3px; margin-right: 4px; }}
</style>
</head>
<body>

<aside class="sidebar">
  <div class="sidebar-header">
    <h1>n8n-workflows-cn</h1>
    <a href="https://github.com/LuckTerence/n8n-workflows-cn" target="_blank">GitHub →</a>
    <div style="margin-top:4px;font-size:12px;color:var(--muted)">{len(workflows)} 个工作流模板</div>
  </div>
  <nav class="sidebar-nav" id="sidebar-nav">
    {nav_html}
  </nav>
</aside>

<main class="main">
  <div class="toolbar">
    <input type="text" class="search-box" id="search" placeholder="搜索工作流...（名称、分类、标签）" oninput="doSearch()" autofocus>
    <button class="badge" id="clear-btn" onclick="clearSearch()">x 清除</button>
    <a href="../INDEX.md" target="_blank" class="badge">完整索引</a>
  </div>
  <div class="scenario-guide visible" id="scenario-guide">
    <h3>按场景快速查找</h3>
    <div class="scenario-list">
      <a href="#!" class="scenario-chip" onclick="filterSub('ai-agent','入门教程');return false;" style="background:rgba(255,215,0,0.12);border-color:#ffd700;">新手推荐</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('ai-agent','对话机器人');return false;">AI 客服机器人</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('workflow-automation','Email & 邮件处理');return false;"> 邮件自动化</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('workflow-automation','销售 & CRM');return false;"> 电商 & 销售</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('finance-analysis','股票 & 市场');return false;">股票分析</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('knowledge-rag','RAG 检索问答');return false;">知识库问答</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('multimodal-ai','图像生成');return false;">AI 绘图</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('devops','监控 & 告警');return false;">运维监控</a>
      <a href="#!" class="scenario-chip" onclick="filterSub('workflow-automation','内容采集 & 研究');return false;">内容采集</a>
    </div>
  </div>
  <div class="results-info" id="results-info">共 {len(workflows)} 个结果</div>
  <div class="list" id="list"></div>
</main>

<script>
const DATA = {json.dumps(workflows, ensure_ascii=False)};

let currentCat = null;
let currentSub = null;
let currentQuery = '';

function render(items) {{
    const list = document.getElementById('list');
    const info = document.getElementById('results-info');
    
    if (items.length === 0) {{
        info.textContent = '没有找到匹配的工作流';
        list.innerHTML = '<div style="text-align:center;padding:60px;color:var(--muted)"> 试试换个搜索词或筛选条件？</div>';
        return;
    }}
    
    info.textContent = `共 ${{items.length}} 个结果`;
    list.innerHTML = items.map(w => `
        <div class="card">
            <div class="card-title">
                <a href="${{w.path}}" target="_blank">${{w.name.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}</a>
                <span class="tier-${{(w.tier||'B').toLowerCase()}}" style="font-size:11px;margin-left:4px;">Tier ${{w.tier||'B'}}</span>
            </div>
            ${{w.desc ? `<div class="card-desc">${{w.desc.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}</div>` : ''}}
            ${{w.apiNeeds && w.apiNeeds.length ? `<div class="card-apis">${{w.apiNeeds.map(a => '<span class="api-tag">'+a+'</span>').join(' ')}}</div>` : ''}}
            <div class="card-meta">
                <span class="tag cat-tag">${{w.categoryIcon}} ${{w.categoryName}}</span>
                <span class="tag sub-tag">${{w.subcategory}}</span>
                ${{w.tags.map(t => `<span class="tag">${{t}}</span>`).join('')}}
            </div>
        </div>
    `).join('');
}}

function getFiltered() {{
    let results = DATA;
    if (currentCat) results = results.filter(w => w.category === currentCat);
    if (currentSub) results = results.filter(w => w.subcategory === currentSub);
    if (currentQuery) {{
        const q = currentQuery.toLowerCase();
        results = results.filter(w => 
            w.name.toLowerCase().includes(q) ||
            w.subcategory.toLowerCase().includes(q) ||
            w.categoryName.toLowerCase().includes(q) ||
            w.tags.some(t => t.toLowerCase().includes(q))
        );
    }}
    return results;
}}

function doSearch() {{
    currentQuery = document.getElementById('search').value.trim();
    document.getElementById('clear-btn').style.display = currentQuery ? 'inline-block' : 'none';
    document.getElementById('scenario-guide').classList.toggle('visible', !currentQuery && !currentCat);
    updateURL();
    render(getFiltered());
}}

function filterSub(cat, sub) {{
    currentCat = cat;
    currentSub = sub;
    document.getElementById('scenario-guide').classList.remove('visible');
    updateActiveNav();
    updateURL();
    render(getFiltered());
}}

function clearSearch() {{
    currentQuery = '';
    currentCat = null;
    currentSub = null;
    document.getElementById('search').value = '';
    document.getElementById('clear-btn').style.display = 'none';
    document.getElementById('scenario-guide').classList.add('visible');
    updateActiveNav();
    updateURL();
    render(DATA);
}}

function updateURL() {{
    const params = new URLSearchParams();
    if (currentCat) params.set('cat', currentCat);
    if (currentSub) params.set('sub', currentSub);
    if (currentQuery) params.set('q', currentQuery);
    const url = params.toString() ? '?' + params.toString() : window.location.pathname;
    history.replaceState(null, '', url);
}}

function applyURLParams() {{
    const params = new URLSearchParams(window.location.search);
    const cat = params.get('cat');
    const sub = params.get('sub');
    const q = params.get('q');
    if (cat || sub) document.getElementById('scenario-guide').classList.remove('visible');
    if (cat) currentCat = cat;
    if (sub) currentSub = sub;
    if (q) {{
        currentQuery = q;
        document.getElementById('search').value = q;
        document.getElementById('clear-btn').style.display = 'inline-block';
    }}
    if (cat || sub) updateActiveNav();
    render(getFiltered());
}}

function updateActiveNav() {{
    document.querySelectorAll('.sub-link').forEach(el => {{
        const c = el.dataset.cat;
        const s = el.dataset.sub;
        el.classList.toggle('active', currentCat === c && currentSub === s);
    }});
}}

function toggleCat(el) {{
    el.nextElementSibling.classList.toggle('collapsed');
}}

applyURLParams();
</script>
</body>
</html>'''
    
    html_path = os.path.join(DOCS_DIR, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Generated {len(workflows)} workflow entries")
    print(f"Site: {html_path}")
    print(f"Data: {data_path}")


if __name__ == "__main__":
    generate_html()
