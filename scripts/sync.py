#!/usr/bin/env python3
"""
批量下载 n8n 工作流并添加中文元数据

用法:
  python scripts/sync.py                    # 下载全部 Tier A 工作流
  python scripts/sync.py --tier A,B         # 下载 Tier A+B
  python scripts/sync.py --category ai-agent # 只下载某个分类
  python scripts/sync.py --limit 50         # 限制数量（测试用）
"""

import json, os, sys, argparse, time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
WORKFLOWS_DIR = BASE / "workflows"

# 精选工作流列表（Tier A — 直接可用）
FEATURED_WORKFLOWS = {
    # AI Agent
    2703: {"title_zh": "AI 日历助手", "desc_zh": "Telegram Bot AI 日程管理", "tier": "B", "category": "ai-agent", "tags": ["ai-agent", "telegram"]},
    3151: {"title_zh": "AI 技术雷达顾问", "desc_zh": "SQL DB + RAG + 路由 Agent 构建技术雷达", "tier": "A", "category": "ai-agent", "tags": ["ai-agent", "rag"]},
    2612: {"title_zh": "AI 数据库对话 Agent", "desc_zh": "用自然语言查询 PostgreSQL 数据库", "tier": "A", "category": "ai-agent", "tags": ["ai-agent", "database"]},
    
    # DevOps
    3229: {"title_zh": "定时启停 n8n 工作流", "desc_zh": "通过 n8n API 按计划启停工作流", "tier": "A", "category": "devops", "tags": ["devops", "n8n-api"]},
    
    # Finance
    5550: {"title_zh": "碳数据 API 接入", "desc_zh": "AI Agent 接入碳排放数据 API", "tier": "A", "category": "finance-analysis", "tags": ["api", "data"]},
    
    # RAG
    3459: {"title_zh": "自适应 RAG 策略", "desc_zh": "查询分类 + 检索优化 + Gemini + Qdrant", "tier": "B", "category": "knowledge-rag", "tags": ["rag", "vector"]},
    4043: {"title_zh": "自适应 RAG 问答", "desc_zh": "Google Gemini + Qdrant 上下文感知问答", "tier": "B", "category": "knowledge-rag", "tags": ["rag", "qa"]},
    
    # Multimodal
    2729: {"title_zh": "AI 视频生成与发布", "desc_zh": "OpenAI + ElevenLabs → YouTube 视频", "tier": "B", "category": "multimodal-ai", "tags": ["video", "ai"]},
    
    # Workflow Automation
    2822: {"title_zh": "AI 摘要生成", "desc_zh": "WordPress 文章自动生成 AI 摘要", "tier": "B", "category": "workflow-automation", "tags": ["wordpress", "ai"]},
}

DOWNLOAD_API = "https://n8nworkflows.xyz/api/download/{}"

def download_one(wf_id, meta):
    """下载单个工作流"""
    url = DOWNLOAD_API.format(wf_id)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'n8n-workflows-cn/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        
        data["_cn_meta"] = {
            "title_zh": meta["title_zh"],
            "description_zh": meta["desc_zh"],
            "category": meta["category"],
            "tier": meta["tier"],
            "tags": meta.get("tags", []),
            "source_id": wf_id,
            "source_url": f"https://n8nworkflows.xyz/workflows/{wf_id}",
            "synced_at": datetime.now().isoformat(),
        }
        
        cat_dir = WORKFLOWS_DIR / meta["category"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        
        original_name = data.get("name", f"workflow-{wf_id}")
        safe_name = original_name.replace("/", "-").replace(":", "-")[:80]
        filename = f"{safe_name}-{wf_id}.json"
        filepath = cat_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return True, filepath.name
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="同步 n8n 工作流")
    parser.add_argument("--tier", default="A,B", help="要下载的 Tier（逗号分隔，如 A,B）")
    parser.add_argument("--category", help="只下载某个分类")
    parser.add_argument("--limit", type=int, default=0, help="限制下载数量")
    args = parser.parse_args()
    
    tiers = set(args.tier.split(","))
    
    to_download = {}
    for wf_id, meta in FEATURED_WORKFLOWS.items():
        if meta["tier"] in tiers:
            if args.category and meta["category"] != args.category:
                continue
            to_download[wf_id] = meta
    
    if args.limit > 0:
        to_download = dict(list(to_download.items())[:args.limit])
    
    print(f"共 {len(to_download)} 个工作流待下载...")
    
    success, failed = 0, 0
    for wf_id, meta in to_download.items():
        ok, msg = download_one(wf_id, meta)
        if ok:
            success += 1
            print(f"  ✅ [{meta['category']}] {meta['title_zh']} → {msg}")
        else:
            failed += 1
            print(f"  ❌ [{meta['category']}] {meta['title_zh']} — {msg}")
        time.sleep(0.3)  # 限速
    
    print(f"\n完成! 成功 {success}, 失败 {failed}")
    
    # 生成 INDEX.md
    generate_index()

def generate_index():
    """生成 CHANGELOG / INDEX"""
    lines = ["# 工作流索引\n", f"> 更新于 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"]
    
    for cat_dir in sorted(WORKFLOWS_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        files = list(cat_dir.glob("*.json"))
        if not files:
            continue
        
        lines.append(f"## {cat_dir.name}\n")
        for f in sorted(files):
            with open(f) as fp:
                data = json.load(fp)
            meta = data.get("_cn_meta", {})
            lines.append(f"- [{meta.get('title_zh', data.get('name', f.name))}]({f.relative_to(BASE)})")
            lines.append(f"  - {meta.get('description_zh', '')} | Tier {meta.get('tier', '?')}\n")
    
    with open(BASE / "INDEX.md", "w") as f:
        f.write("\n".join(lines))
    
    print(f"\n📋 INDEX.md 已更新 ({len(lines)} 行)")

if __name__ == "__main__":
    main()
