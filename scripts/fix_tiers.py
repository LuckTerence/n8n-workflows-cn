#!/usr/bin/env python3
"""Honest tier: downgrade A/A-adapted with Gmail/Google to B."""

import json, os

BASE = "/Users/terencesai/WorkBuddy/2026-06-17-04-19-06/n8n-workflows-cn"
WF_DIR = os.path.join(BASE, "workflows")

FOREIGN = [
    ("gmail", "Gmail", "QQ邮箱/企业微信"),
    ("google sheets", "Google Sheets", "飞书多维表格"),
    ("googlesheet", "Google Sheets", "飞书多维表格"),
    ("google drive", "Google Drive", "阿里云OSS"),
    ("googledrive", "Google Drive", "阿里云OSS"),
    ("google docs", "Google Docs", "飞书文档"),
    ("slack", "Slack", "飞书群机器人"),
    ("twilio", "Twilio", "腾讯云短信"),
    ("stripe", "Stripe", "微信支付"),
    ("zoom", "Zoom", "腾讯会议"),
    ("notion", "Notion", "飞书文档/语雀"),
    ("supabase", "Supabase", "腾讯云CloudBase"),
    ("pinecone", "Pinecone", "Milvus/腾讯云向量库"),
]

def run():
    d, n = 0, 0
    for cat in sorted(os.listdir(WF_DIR)):
        cp = os.path.join(WF_DIR, cat)
        if not os.path.isdir(cp) or cat.startswith("."): continue
        for wf in sorted(os.listdir(cp)):
            wp = os.path.join(cp, wf)
            if not os.path.isdir(wp): continue
            jf = os.path.join(wp, "workflow.json")
            rf = os.path.join(wp, "readme.md")
            if not os.path.exists(jf): continue
            with open(jf) as f: data = json.load(f)
            meta = data.get("_cn_meta", {})
            tier = meta.get("tier", "")
            if tier not in ("A", "A-adapted"): continue
            ns = json.dumps(data.get("nodes", [])).lower()
            found = [(name, repl) for kw, name, repl in FOREIGN if kw in ns]
            if not found: continue
            has_gmail_google = any("gmail" in name.lower() or "google" in name.lower() for name, _ in found)
            if has_gmail_google:
                data["_cn_meta"]["tier"] = "B"
                data["_cn_meta"]["foreign_services"] = list(set(n for n,_ in found))
                data["_cn_meta"]["upgrade_note"] = "、".join(f"{n}→{r}" for n,r in found)
                with open(jf, "w") as f: json.dump(data, f, ensure_ascii=False, indent=2)
                if os.path.exists(rf):
                    with open(rf) as f: c = f.read()
                    for old in ["适配等级：A-adapted", "适配等级：A"]:
                        c = c.replace(old, f"适配等级：B（需替换{'/'.join(set(n for n,_ in found))})")
                    with open(rf, "w") as f: f.write(c)
                d += 1
            else:
                data["_cn_meta"]["foreign_services"] = list(set(n for n,_ in found))
                with open(jf, "w") as f: json.dump(data, f, ensure_ascii=False, indent=2)
                n += 1
    print(f"降级→B: {d} | 标记: {n}")

if __name__ == "__main__":
    run()
