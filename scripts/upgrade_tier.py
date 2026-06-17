#!/usr/bin/env python3
"""Batch upgrade B-tier workflows: OpenAI→DeepSeek, update tier markers."""

import json
import os
import shutil

BASE = "/Users/terencesai/WorkBuddy/2026-06-17-04-19-06/n8n-workflows-cn"
WF_DIR = os.path.join(BASE, "workflows")

def patch_openai_node(node):
    """Replace OpenAI model settings with DeepSeek."""
    node_type = node.get("type", "")
    
    if "OpenAI" in node_type or node_type.startswith("@n8n/n8n-nodes-langchain"):
        params = node.get("parameters", {})
        options = params.get("options", {})
        
        if "Chat Model" in node_type or "Llm" in node_type:
            # OpenAI Chat Model → DeepSeek
            options["baseURL"] = "https://api.deepseek.com"
            params["model"] = "deepseek-chat"
            params["options"] = options
            node["parameters"] = params
            return "openai_chat→deepseek"
            
        elif "Embeddings" in node_type:
            params["model"] = "text-embedding-3-small"
            node["parameters"] = params
            return "openai_embeddings→compat"
    
    # Check node name in n8n community nodes
    node_name = node.get("name", "")
    type_str = json.dumps(node)
    if "openai" in type_str.lower():
        params = node.get("parameters", {})
        if "model" in params:
            # Generic OpenAI → compatible
            if "chat" in node_type.lower() or "llm" in node_type.lower():
                options = params.get("options", {})
                options["baseURL"] = "https://api.deepseek.com"
                params["model"] = "deepseek-chat"
                params["options"] = options
                node["parameters"] = params
                return "generic_openai→deepseek"
    
    return None


def upgrade_workflow(cat, wf_dir):
    """Upgrade a single workflow."""
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
    
    for node in nodes:
        result = patch_openai_node(node)
        if result:
            changes.append(result)
    
    if not changes:
        return None  # Nothing to auto-upgrade
    
    # Update tier
    data["_cn_meta"]["tier"] = "A-adapted"
    data["_cn_meta"]["upgraded_at"] = "2026-06-17"
    
    # Backup original
    shutil.copy2(jf, jf + ".bak")
    
    # Write patched file
    with open(jf, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Update readme tier label
    if os.path.exists(rdf):
        with open(rdf, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(
            "适配等级：B（核心链路通了，边角节点可能要自己调）",
            "适配等级：A-adapted（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）"
        )
        content = content.replace(
            "适配等级：B",
            "适配等级：A-adapted"
        )
        with open(rdf, "w", encoding="utf-8") as f:
            f.write(content)
    
    return changes


def main():
    results = {}
    for cat in sorted(os.listdir(WF_DIR)):
        cat_path = os.path.join(WF_DIR, cat)
        if not os.path.isdir(cat_path) or cat.startswith("."):
            continue
        for wf_dir in sorted(os.listdir(cat_path)):
            wf_path = os.path.join(cat_path, wf_dir)
            if not os.path.isdir(wf_path):
                continue
            changes = upgrade_workflow(cat, wf_dir)
            if changes:
                title = wf_dir
                jf = os.path.join(wf_path, "workflow.json")
                with open(jf) as f:
                    meta = json.load(f).get("_cn_meta", {})
                    title = meta.get("title_zh", wf_dir)
                results[title] = changes
    
    print(f"Upgraded {len(results)} workflows to A-adapted:\n")
    for name, changes in sorted(results.items()):
        print(f"  OK {name}")
        for c in set(changes):
            print(f"     • {c}")
    
    if not results:
        print("No workflows needed upgrading (all already A-tier)")
    
    return len(results)


if __name__ == "__main__":
    count = main()
    print(f"\nTotal: {count} workflows upgraded")
