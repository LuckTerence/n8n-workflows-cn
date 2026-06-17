import json, os, sys, requests
from pathlib import Path

"""
从 n8nworkflows.xyz 批量下载工作流 JSON 文件
用法: python scripts/download.py
"""

# 从本地分析结果读取工作流列表
WORKFLOWS_FILE = "/tmp/all_workflows.txt"
DOWNLOAD_API = "https://n8nworkflows.xyz/api/download/{}"
OUTPUT_DIR = Path(__file__).parent.parent / "workflows"

# 分类映射（根据工作流名称关键词自动分类）
CATEGORIES = {
    "ai-agent": ["AI Agent", "agent", "MCP", "Agentic", "autonomous"],
    "devops": ["webhook", "API", "monitor", "backup", "deploy", "Docker", "CI/CD", "alert", "REST"],
    "finance-analysis": ["stock", "crypto", "trading", "CoinGecko", "Binance", "finance", "portfolio"],
    "knowledge-rag": ["RAG", "knowledge base", "Ollama", "PGVector", "Qdrant", "embedding"],
    "multimodal-ai": ["image", "video", "voice", "audio", "OCR", "transcription", "TTS"],
    "workflow-automation": ["飞书", "企业微信", "钉钉", "wecom", "feishu", "Telegram", "RSS", "sync", "automation"],
}

def extract_workflow_id(name):
    """从 '工作流名称-12345' 提取 ID"""
    parts = name.rsplit("-", 1)
    if len(parts) == 2 and parts[1].isdigit():
        return parts[1]
    return None

def determine_category(name):
    """根据工作流名称自动分类"""
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in name.lower():
                return cat
    return "workflow-automation"  # 默认分类

def download_workflow(wf_id, wf_name, category):
    """下载单个工作流"""
    url = DOWNLOAD_API.format(wf_id)
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        
        # 添加中文元数据
        data["_cn_meta"] = {
            "original_name": wf_name,
            "category": category,
            "source": f"n8nworkflows.xyz/{wf_id}",
        }
        
        # 保存
        safe_name = wf_name.replace("/", "-").replace(":", "-")[:80]
        filename = f"{safe_name}-{wf_id}.json"
        filepath = OUTPUT_DIR / category / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return True, filename
    except Exception as e:
        return False, str(e)

def main():
    if not os.path.exists(WORKFLOWS_FILE):
        print(f"错误: 找不到工作流列表文件 {WORKFLOWS_FILE}")
        print("请先运行 analysis.py 生成工作流列表")
        sys.exit(1)
    
    with open(WORKFLOWS_FILE) as f:
        workflows = [line.strip() for line in f if line.strip() and not line.startswith("---")]
    
    print(f"共 {len(workflows)} 个工作流，开始下载...")
    
    success, failed = 0, 0
    for i, wf in enumerate(workflows):
        wf_id = extract_workflow_id(wf)
        if not wf_id:
            continue
        
        category = determine_category(wf)
        ok, msg = download_workflow(wf_id, wf, category)
        
        if ok:
            success += 1
        else:
            failed += 1
        
        if (i + 1) % 100 == 0:
            print(f"  进度: {i+1}/{len(workflows)} (成功 {success}, 失败 {failed})")
    
    print(f"\n完成! 成功: {success}, 失败: {failed}")

if __name__ == "__main__":
    main()
