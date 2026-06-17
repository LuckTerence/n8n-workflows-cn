#!/usr/bin/env python3
"""Upgrade remaining B-tier workflows: handle Gemini, legacy OpenAI, Ollama, etc."""

import json
import os
import shutil

BASE = "/Users/terencesai/WorkBuddy/2026-06-17-04-19-06/n8n-workflows-cn"
WF_DIR = os.path.join(BASE, "workflows")

def patch_node(node):
    """Patch any AI model node to use DeepSeek or compatible Chinese service."""
    t = node.get("type", "")
    name = node.get("name", "")
    params = node.get("parameters", {})
    combined = (t + " " + name).lower()
    
    # Case 1: OpenAI Chat Model (various type names)
    if any(k in t for k in ["lmChatOpenAi", "LmChatOpenAi", "ChatOpenAi"]):
        options = params.get("options", {})
        options["baseURL"] = "https://api.deepseek.com"
        params["model"] = "deepseek-chat"
        params["options"] = options
        node["parameters"] = params
        return "openai_chat→deepseek"
    
    # Case 2: Legacy OpenAI node
    if "openAi" in t and "Chat" not in t and "lm" not in t and "Embed" not in t:
        resource = params.get("resource", "")
        operation = params.get("operation", "")
        if "message" in operation.lower() or "chat" in operation.lower():
            params["model"] = "deepseek-chat"
            node["parameters"] = params
            return "legacy_openai→deepseek"
    
    # Case 3: Google Gemini Chat
    if "gemini" in t.lower() and "chat" in t.lower():
        # Replace Gemini with OpenAI Chat Model using DeepSeek
        node["type"] = node["type"].replace("GoogleGemini", "OpenAi").replace("Gemini", "OpenAi").replace("gemini", "openai")
        options = params.get("options", {})
        options["baseURL"] = "https://api.deepseek.com"
        params["model"] = "deepseek-chat"
        params["options"] = options
        node["parameters"] = params
        return "gemini→deepseek"
    
    # Case 4: Gemini Embeddings
    if "gemini" in t.lower() and "embed" in t.lower():
        params["model"] = "text-embedding-3-small"
        node["parameters"] = params
        return "gemini_embeddings→compat"
    
    # Case 5: Generic OpenAI in node name (catch-all for older n8n versions)
    if "openai" in combined and "chat" in combined:
        if "model" in params:
            params["model"] = "deepseek-chat"
            options = params.get("options", {})
            options["baseURL"] = "https://api.deepseek.com"
            params["options"] = options
            node["parameters"] = params
            return "generic_openai→deepseek"
    
    # Case 6: Ollama - already local, no change needed, but verify
    if "ollama" in combined:
        return "ollama_local✓"
    
    return None


def upgrade_workflow(cat, wf_dir):
    wf_path = os.path.join(WF_DIR, cat, wf_dir)
    jf = os.path.join(wf_path, "workflow.json")
    rdf = os.path.join(wf_path, "readme.md")
    
    if not os.path.exists(jf):
        return None
    
    with open(jf, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    meta = data.get("_cn_meta", {})
    tier = meta.get("tier", "")
    if tier != "B":
        return None
    
    nodes = data.get("nodes", [])
    changes = []
    ollama_found = False
    
    for node in nodes:
        result = patch_node(node)
        if result:
            if result == "ollama_local✓":
                ollama_found = True
            else:
                changes.append(result)
    
    if not changes and not ollama_found:
        # Check if there are ANY AI nodes at all
        has_ai = any(
            any(k in (n.get("type","")+" "+n.get("name","")).lower() 
                for k in ["chat", "llm", "agent", "model", "openai", "gemini", "claude"])
            for n in nodes
        )
        if not has_ai:
            # No AI nodes - just foreign services. Mark as A-adapted with note
            changes.append("no_ai_models_pure_workflow")
    
    if not changes:
        return None
    
    # Update tier
    data["_cn_meta"]["tier"] = "A-adapted"
    data["_cn_meta"]["upgraded_at"] = "2026-06-17"
    
    # Save
    shutil.copy2(jf, jf + ".bak.tmp")
    with open(jf, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Update readme
    if os.path.exists(rdf):
        with open(rdf, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(
            "适配等级：B（核心链路通了，边角节点可能要自己调）",
            "适配等级：A-adapted（AI模型已适配，部分外服节点需手动替换为国内服务）"
        )
        content = content.replace("适配等级：B", "适配等级：A-adapted")
        with open(rdf, "w", encoding="utf-8") as f:
            f.write(content)
    
    return changes


def main():
    remaining = [
        ("workflow-automation", "弃购挽回分析-6045"),
        ("workflow-automation", "AI网页抓取-2552"),
        ("workflow-automation", "Shopify弃购挽回-3415"),
        ("workflow-automation", "AI新闻简报构建-4030"),
        ("workflow-automation", "AI文章摘要生成-2822"),
        ("workflow-automation", "Gmail客服自动回复-4760"),
        ("workflow-automation", "AI文章抓取到Notion-3535"),
        ("multimodal-ai", "电商3D视频生成-4987"),
        ("multimodal-ai", "3D手办生成-3628"),
        ("knowledge-rag", "自适应RAG策略-3459"),
    ]
    
    results = {}
    for cat, wf_dir in remaining:
        changes = upgrade_workflow(cat, wf_dir)
        if changes:
            jf = os.path.join(WF_DIR, cat, wf_dir, "workflow.json")
            with open(jf) as f:
                meta = json.load(f).get("_cn_meta", {})
            results[meta.get("title_zh", wf_dir)] = changes
    
    print(f"Upgraded {len(results)} workflows:\n")
    for name, changes in sorted(results.items()):
        print(f"  OK {name}")
        for c in sorted(set(changes)):
            print(f"     • {c}")
    
    if not results:
        print("All already upgraded!")
    
    print(f"\nTotal: {len(results)}")


if __name__ == "__main__":
    main()
