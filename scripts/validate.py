#!/usr/bin/env python3
"""Validate all workflows: JSON format, _cn_meta, readme, directory structure."""

import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF_DIR = os.path.join(BASE, "workflows")

VALID_CATEGORIES = {
    "ai-agent", "devops", "finance-analysis",
    "knowledge-rag", "multimodal-ai", "workflow-automation",
}
VALID_TIERS = {"A", "A-adapted", "B", "B-adapted", "C", "C-adapted"}

errors = []
warnings = []


def check_dir_name(wf_dir, cat):
    """Validate directory naming: should be {Name}-{ID} or {中文名}-{ID}"""
    parts = wf_dir.rsplit("-", 1)
    if len(parts) != 2:
        errors.append(f"{cat}/{wf_dir}: 目录名不符合 '名称-ID' 格式")
        return
    try:
        int(parts[1])
    except ValueError:
        errors.append(f"{cat}/{wf_dir}: ID 部分 '{parts[1]}' 不是数字")


def check_workflow_json(path, cat, wf_dir):
    """Validate workflow.json"""
    if not os.path.exists(path):
        errors.append(f"{cat}/{wf_dir}: 缺少 workflow.json")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"{cat}/{wf_dir}: workflow.json 不是合法 JSON — {e}")
        return
    except Exception as e:
        errors.append(f"{cat}/{wf_dir}: 读取 workflow.json 失败 — {e}")
        return

    # Check _cn_meta
    meta = data.get("_cn_meta")
    if not meta:
        errors.append(f"{cat}/{wf_dir}: workflow.json 缺少 _cn_meta 字段")
        return

    required = {
        "title_zh": str,
        "category": str,
        "tier": str,
        "source_id": (int, type(None)),
        "synced_at": str,
    }

    optional = {
        "description_zh": str,
    }

    for field, expected_type in required.items():
        val = meta.get(field)
        if val is None:
            errors.append(f"{cat}/{wf_dir}: _cn_meta 缺少 '{field}' 字段")
            continue
        if not isinstance(val, expected_type):
            errors.append(
                f"{cat}/{wf_dir}: _cn_meta.{field} 类型错误 "
                f"(期望 {expected_type.__name__}, 实际 {type(val).__name__})"
            )

    for field, expected_type in optional.items():
        val = meta.get(field)
        if val is not None and not isinstance(val, expected_type):
            warnings.append(
                f"{cat}/{wf_dir}: _cn_meta.{field} 类型错误 "
                f"(期望 {expected_type.__name__}, 实际 {type(val).__name__})"
            )
        if val is None:
            warnings.append(f"{cat}/{wf_dir}: _cn_meta 建议添加 '{field}' 字段")

    # Check category
    category_val = meta.get("category", "")
    if category_val not in VALID_CATEGORIES:
        errors.append(
            f"{cat}/{wf_dir}: _cn_meta.category '{category_val}' "
            f"不在有效值 {VALID_CATEGORIES} 中"
        )

    # Check tier
    tier_val = meta.get("tier", "")
    if tier_val not in VALID_TIERS:
        errors.append(
            f"{cat}/{wf_dir}: _cn_meta.tier '{tier_val}' "
            f"不在有效值 {VALID_TIERS} 中"
        )

    # Check category matches directory
    if meta.get("category") != cat:
        warnings.append(
            f"{cat}/{wf_dir}: _cn_meta.category '{meta.get('category')}' "
            f"与目录分类 '{cat}' 不一致"
        )

    # Basic n8n structure check
    nodes = data.get("nodes", [])
    if not isinstance(nodes, list):
        errors.append(f"{cat}/{wf_dir}: workflow.json 的 'nodes' 不是数组")
    connections = data.get("connections", {})
    if not isinstance(connections, dict):
        errors.append(f"{cat}/{wf_dir}: workflow.json 的 'connections' 不是对象")


def check_readme(path, cat, wf_dir):
    """Validate readme.md exists and has basic content."""
    if not os.path.exists(path):
        warnings.append(f"{cat}/{wf_dir}: 缺少 readme.md")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"{cat}/{wf_dir}: 读取 readme.md 失败 — {e}")
        return

    if len(content.strip()) < 50:
        warnings.append(f"{cat}/{wf_dir}: readme.md 内容太少 ({len(content)} 字符)")


def main():
    total = 0
    for cat in sorted(os.listdir(WF_DIR)):
        cat_path = os.path.join(WF_DIR, cat)
        if not os.path.isdir(cat_path) or cat.startswith("."):
            continue
        if cat not in VALID_CATEGORIES:
            warnings.append(f"发现未知分类目录: {cat}")
            continue

        for wf_dir in sorted(os.listdir(cat_path)):
            wf_path = os.path.join(cat_path, wf_dir)
            if not os.path.isdir(wf_path):
                continue
            total += 1

            check_dir_name(wf_dir, cat)
            check_workflow_json(os.path.join(wf_path, "workflow.json"), cat, wf_dir)
            check_readme(os.path.join(wf_path, "readme.md"), cat, wf_dir)

    # Print results
    print(f"\n{'='*60}")
    print(f"  n8n-workflows-cn 验证报告")
    print(f"{'='*60}")
    print(f"  总工作流: {total}")
    print(f"  错误: {len(errors)}")
    print(f"  警告: {len(warnings)}")
    print(f"{'='*60}\n")

    if errors:
        print("❌ 错误:")
        for e in errors:
            print(f"  • {e}")
        print()

    if warnings:
        print("⚠️  警告:")
        for w in warnings:
            print(f"  • {w}")
        print()

    if not errors:
        print("✅ 所有验证通过！")
        return 0
    else:
        print(f"❌ 发现 {len(errors)} 个错误")
        return 1


if __name__ == "__main__":
    sys.exit(main())
