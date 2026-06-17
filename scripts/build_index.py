#!/usr/bin/env python3
"""Build INDEX.md with sub-categories and Chinese descriptions for all 1480 workflows."""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF_DIR = os.path.join(BASE, "workflows")

# ── Category metadata ──────────────────────────────────────────────
CATEGORIES = {
    "ai-agent": {
        "name": "AI Agent",
        "desc": "AI 智能体、聊天机器人、多智能体协作",
        "count": 93,
        "order": 0,
    },
    "devops": {
        "name": "DevOps",
        "desc": "服务器管理、API 开发、MCP Server、监控告警、自动部署",
        "count": 153,
        "order": 1,
    },
    "finance-analysis": {
        "name": "Finance Analysis",
        "desc": "股票分析、加密货币、交易信号、欺诈检测、市场数据",
        "count": 25,
        "order": 2,
    },
    "knowledge-rag": {
        "name": "Knowledge RAG",
        "desc": "向量数据库、RAG 检索增强生成、文档问答、语义缓存",
        "count": 47,
        "order": 3,
    },
    "multimodal-ai": {
        "name": "Multimodal AI",
        "desc": "图像生成、语音合成、视频生成、音频转录、3D 内容生成",
        "count": 52,
        "order": 4,
    },
    "workflow-automation": {
        "name": "Workflow Automation",
        "desc": "业务流程自动化、邮件处理、数据采集、社交媒体、CRM 集成",
        "count": 1110,
        "order": 5,
    },
}


# ── Sub-category classification rules ─────────────────────────────
# Each rule: (sub_name, sub_count_approx, match_fn) where match_fn takes
# the lowercase dirname and returns True if it belongs.

# ─────────────────── AI Agent ───────────────────
def _ai_agent_rules():
    return [
        ("Agent 框架", 2, lambda n: any(k in n for k in ["langchain", "agent framework"])),
        ("MCP 工具 & 集成", 18, lambda n: "mcp" in n and "smcp" not in n),
        ("个人助理", 2, lambda n: "personal assistant" in n or "personal ai agent" in n),
        ("入门教程", 2, lambda n: any(k in n for k in ["build your first ai agent", "create your first ai agent"])),
        ("多智能体", 4, lambda n: any(k in n for k in ["multi-agent", "multi agent", "dual ai agent", "scalable multi-agent", "evaluate tool usage"])),
        ("多模态 Agent", 1, lambda n: "video" in n and "agent" in n),
        ("对话机器人", 30, lambda n: "chatbot" in n or "聊天" in n),
        ("搜索 & 研究 Agent", 2, lambda n: any(k in n for k in ["web content", "internet archive search"])),
        ("消息平台机器人", 6, lambda n: any(k in n for k in ["telegram", "whatsapp"])),
        ("金融 Agent", 3, lambda n: any(k in n for k in ["payment", "token"])),
        ("其他", None, lambda n: True),
    ]


def _devops_rules():
    return [
        ("API 集成 & Webhook", 78, lambda n: any(k in n for k in ["api", "webhook", "http request", "endpoint", "rest", "web service"])),
        ("CI/CD & 部署", 9, lambda n: any(k in n for k in ["deploy", "docker update", "kubernetes", "coolify", "auto n8n updater", "package & deploy"])),
        ("MCP Server 构建", 11, lambda n: "mcp server" in n),
        ("代码管理", 2, lambda n: any(k in n for k in ["privacy", "code"])),
        ("备份 & 恢复", 3, lambda n: any(k in n for k in ["backup", "restore"])),
        ("安全 & 认证", 2, lambda n: any(k in n for k in ["security", "domain check", "cyber"])),
        ("服务器 & 云", 9, lambda n: any(k in n for k in ["server", "linux", "vps", "lamp", "mern", "nextcloud"])),
        ("监控 & 告警", 38, lambda n: any(k in n for k in ["alert", "notif", "monitor", "watchdog"])),
        ("其他", None, lambda n: True),
    ]


def _finance_rules():
    return [
        ("AI 投顾", 2, lambda n: any(k in n for k in ["invoice", "financial news digest"])),
        ("股票 & 市场", 22, lambda n: any(k in n for k in ["stock", "crypto", "forex", "market", "portfolio", "trading", "coin"])),
        ("风控 & 合规", 1, lambda n: "fraud" in n),
    ]


def _knowledge_rag_rules():
    return [
        ("RAG 检索问答", 38, lambda n: "rag" in n or "chat with" in n or "retriev" in n or "问答" in n),
        ("向量数据库", 8, lambda n: any(k in n for k in ["vector", "qdrant", "milvus", "pinecone", "pgvector", "embedding"])),
        ("其他", None, lambda n: True),
    ]


def _multimodal_rules():
    return [
        ("3D 生成", 3, lambda n: "3d" in n or "手办" in n),
        ("图像分析", 3, lambda n: "vision" in n or "发票识别" in n or "transaction" in n),
        ("图像生成", 9, lambda n: any(k in n for k in ["image", "图片", "flux", "banana", "stock image"])),
        ("视频生成", 4, lambda n: "video" in n),
        ("语音 & 音频", 29, lambda n: any(k in n for k in ["voice", "audio", "speech", "tts", " whisper", "call", "phone", "vapi", "retell"])),
        ("其他", None, lambda n: True),
    ]


def _workflow_rules():
    return [
        # Order matters: first-match-wins. More specific rules first.
        ("AI 增强工作流", 71, lambda n: any(k in n for k in [
            "ai-powered", "ai agent", "ai model", "ai prompt",
            "ai image", "ai video", "ai safety", "ai automated",
            "ai summar", "ai chat", "openai", " chatgpt",
            "llm ", "-llm", " llm ", "groq", "ollama",
            "ai content", "ai ocr", "ai-driven", "ai-enhanced",
            "ai resume", "ai cv",
        ])),
        ("电商 & 营销", 50, lambda n: any(k in n for k in [
            "e-commerce", "ecommerce", "product catalog", "magento",
            "woocommerce", "shopify", "ad creative", "marketing",
            "ad campaign", "pricing", "dynamic pricing",
        ])),
        ("ERP & 财务", 35, lambda n: any(k in n for k in [
            "sap ", "netsuite", "quickbook", "invoice",
            "accounting", "currency", "bank transaction",
            "financial report", "budget", "fx ", " foreign exchange",
        ])),
        ("CRM & 客服", 55, lambda n: any(k in n for k in [
            "crm", "customer support", "helpdesk", "lead ",
            "zammad", "kommo", "klicktipp", "aloware", "ninjapipe",
            "stucco", "meldflow",
        ])),
        ("项目管理", 25, lambda n: any(k in n for k in [
            "jira", "asana", "clickup", "trello", "notion",
            "syncro", "clockify", "easy redmine", "project ",
            "task management", "todo", "smenso",
        ])),
        ("消息平台 & Bot", 90, lambda n: any(k in n for k in [
            "telegram", "whatsapp", "slack", "discord",
            "mattermost", "line ", "zalo", "wechat", "bot ",
            "-bot", "bitrix", "dialogflow",
        ])),
        ("邮件 & 通讯", 80, lambda n: any(k in n for k in [
            "email", "mail", "newsletter", "smtp", "gmail",
            "outlook", "imap", "mandrill", "mailerlite",
        ])),
        ("日历 & 日程", 30, lambda n: any(k in n for k in [
            "calendar", "schedule", "booking", "appointment", "meeting",
        ])),
        ("社交媒体 & 内容", 120, lambda n: any(k in n for k in [
            "social media", "social post", "blog", "content creator",
            "x ", "twitter", "bluesky", "mastodon", "linkedin",
            "instagram", "facebook", "youtube", "seo", "rss",
            "postiz", "blotato", "bannerbear",
        ])),
        ("数据采集 & 爬虫", 65, lambda n: any(k in n for k in [
            "scrape", "crawl", "extract", "data table",
            "firecrawl", "airtop", "scrapegraph",
        ])),
        ("文件 & 存储", 55, lambda n: any(k in n for k in [
            "google drive", "google sheet", "google doc",
            "excel", "csv", "pdf", "file", "upload",
            "download", "storage", "nextcloud", "s3",
            "ftp", "dropbox",
        ])),
        ("表单 & 问卷", 40, lambda n: any(k in n for k in [
            "form", "survey", "questionnaire", "poll",
            "gravity forms",
        ])),
        ("API 集成 & 自动化", 187, lambda n: any(k in n for k in [
            "api", "webhook", "http request", "http router",
            "rest api", "crud", "xmlrpc",
        ])),
        ("通知 & 告警", 70, lambda n: any(k in n for k in [
            "alert", "notif", "pushover", "signl4",
        ])),
        ("其他", None, lambda n: True),
    ]


RULES = {
    "ai-agent": _ai_agent_rules(),
    "devops": _devops_rules(),
    "finance-analysis": _finance_rules(),
    "knowledge-rag": _knowledge_rag_rules(),
    "multimodal-ai": _multimodal_rules(),
    "workflow-automation": _workflow_rules(),
}


# ── Chinese description generator ──────────────────────────────────
def make_chinese_desc(name_lower, name_original, category):
    """Generate a brief Chinese description from the workflow name."""
    pairs = {
        "chatbot": "AI 聊天机器人",
        "chat": "AI 对话",
        "agent": "AI 智能体",
        "mcp": "MCP 协议集成",
        "rag": "RAG 检索增强",
        "telegram": "Telegram 机器人",
        "whatsapp": "WhatsApp 机器人",
        "line ": "LINE 集成",
        "slack": "Slack 集成",
        "email": "邮件自动化",
        "gmail": "Gmail 自动化",
        "api": "API 接口",
        "webhook": "Webhook 集成",
        "backup": "自动备份",
        "restore": "数据恢复",
        "deploy": "自动部署",
        "docker": "Docker 管理",
        "kubernetes": "K8s 运维",
        "monitor": "系统监控",
        "alert": "告警通知",
        "notif": "消息通知",
        "stock": "股票分析",
        "crypto": "加密货币",
        "forex": "外汇交易",
        "market": "市场数据",
        "vector": "向量存储",
        "qdrant": "Qdrant 向量库",
        "pinecone": "Pinecone 向量库",
        "image": "图片生成",
        "video": "视频生成",
        "voice": "语音处理",
        "audio": "音频处理",
        "scrape": "数据采集",
        "crawl": "网页爬取",
        "form": "表单处理",
        "invoice": "发票处理",
        "payment": "支付集成",
        "seo": "SEO 优化",
        "blog": "博客内容",
        "social": "社交平台",
        "job": "求职招聘",
        "interview": "面试系统",
        "hr": "HR 人事",
        "lead": "线索管理",
        "crm": "CRM 客户",
        "ticket": "工单管理",
        "weather": "天气信息",
        "news": "新闻聚合",
        "pdf": "PDF 文档",
        "sheet": "表格处理",
        "database": "数据库操作",
        "postgresql": "PostgreSQL",
        "mysql": "MySQL 管理",
        "sql": "SQL 查询",
        "ssh": "SSH 远程",
        "linux": "Linux 管理",
        "server": "服务器管理",
        "workflow": "工作流管理",
        "automate": "流程自动化",
        "n8n": "n8n 运维",
        "token": "Token 管理",
        "auth": "认证集成",
        "transcribe": "语音转录",
        "tts": "文本转语音",
        "search": "智能搜索",
        "recommend": "推荐系统",
        "summary": "AI 摘要",
        "translate": "翻译服务",
    }

    descs = []
    for key, cn in pairs.items():
        if key in name_lower:
            descs.append(cn)

    if not descs:
        # Fallback: use the first few words
        words = name_original.split(" ")[:5]
        descs.append("自动化工作流")

    return "、".join(descs[:3])


# ── Main build logic ───────────────────────────────────────────────
def get_all_workflows():
    """Scan all workflow directories and return [(category, dirname, readme_path), ...]"""
    workflows = []
    for cat in sorted(os.listdir(WF_DIR)):
        cat_path = os.path.join(WF_DIR, cat)
        if not os.path.isdir(cat_path) or cat.startswith("."):
            continue
        if cat not in CATEGORIES:
            continue
        for wf_dir in sorted(os.listdir(cat_path)):
            wf_path = os.path.join(cat_path, wf_dir)
            if not os.path.isdir(wf_path):
                continue
            readme_path = os.path.join(wf_path, "readme.md")
            workflows.append((cat, wf_dir, readme_path, wf_path))
    return workflows


def classify_workflow(category, dirname_lower):
    """Return sub-category name for a workflow."""
    rules = RULES.get(category, [("其他", None, lambda n: True)])
    for sub_name, _, match_fn in rules:
        if match_fn(dirname_lower):
            return sub_name
    return "其他"


def build():
    workflows = get_all_workflows()

    # Group by category → sub-category → [(dirname, desc, dirpath)]
    tree = {}
    for cat, wf_dir, readme_path, wf_path in workflows:
        dirname_lower = wf_dir.lower()
        sub = classify_workflow(cat, dirname_lower)
        desc = make_chinese_desc(dirname_lower, wf_dir, cat)
        # Shorten the link text: use the directory name
        if cat not in tree:
            tree[cat] = {}
        if sub not in tree[cat]:
            tree[cat][sub] = []
        tree[cat][sub].append((wf_dir, desc))

    # Sort categories by order
    ordered_cats = sorted(tree.keys(), key=lambda c: CATEGORIES[c]["order"])

    def write_category_index(cat, prefix=""):
        """Generate index lines for a single category with optional path prefix."""
        meta = CATEGORIES[cat]
        cat_workflows = tree[cat]
        total = sum(len(v) for v in cat_workflows.values())
        sub_order = {s: i for i, (s, _, _) in enumerate(RULES.get(cat, []))}
        sorted_subs = sorted(cat_workflows.keys(), key=lambda s: sub_order.get(s, 999))

        lines = []
        lines.append(f"## {meta['name']}")
        lines.append("")
        lines.append(f"共 {total} 个工作流。{meta['desc']}。")
        lines.append("")

        for sub_name in sorted_subs:
            entries = cat_workflows[sub_name]
            if not entries:
                continue
            lines.append(f'<details>')
            lines.append(f'<summary><b>{sub_name}</b>（{len(entries)} 个）</summary>')
            lines.append("")
            for wf_dir, desc in sorted(entries):
                link = f"{prefix}workflows/{cat}/{wf_dir}/"
                display_clean = wf_dir.replace("[", "(").replace("]", ")")
                lines.append(f"- [{display_clean}]({link}) — {desc}")
            lines.append("")
            lines.append(f'</details>')
            lines.append("")
        return lines

    # ── Main INDEX.md (repo root) ──
    lines = []
    lines.append("# 工作流索引")
    lines.append("")
    lines.append(f"> 按分类和场景整理的 {len(workflows)} 个 n8n 工作流模板目录，点击链接查看工作流详情说明。")
    lines.append("")
    lines.append("## 目录")
    lines.append("")

    for cat in ordered_cats:
        meta = CATEGORIES[cat]
        lines.append(f"- [{meta['name']}](index/INDEX-{cat}.md)（{sum(len(v) for v in tree[cat].values())} 个）— {meta['desc']}")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("点击分类名称查看各分类的详细工作流列表。")
    lines.append("")

    for cat in ordered_cats:
        lines.extend(write_category_index(cat, prefix=""))

    output_path = os.path.join(BASE, "INDEX.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Written {len(workflows)} workflows to {output_path}")

    # ── Per-category INDEX files (index/ directory) ──
    os.makedirs(os.path.join(BASE, "index"), exist_ok=True)
    for cat in ordered_cats:
        meta = CATEGORIES[cat]
        total = sum(len(v) for v in tree[cat].values())
        cat_lines = []
        cat_lines.append(f"# {meta['name']} — 工作流索引")
        cat_lines.append("")
        cat_lines.append(f"> {meta['desc']}，共 {total} 个工作流模板。")
        cat_lines.append("")
        cat_lines.append("[← 返回总索引](../INDEX.md)")
        cat_lines.append("")
        cat_lines.append("---")
        cat_lines.append("")
        cat_lines.extend(write_category_index(cat, prefix="../"))

        cat_path = os.path.join(BASE, f"index/INDEX-{cat}.md")
        with open(cat_path, "w", encoding="utf-8") as f:
            f.write("\n".join(cat_lines) + "\n")
        print(f"  → index/INDEX-{cat}.md ({total} workflows)")

    print(f"File size: {len(lines)} lines")


if __name__ == "__main__":
    build()
