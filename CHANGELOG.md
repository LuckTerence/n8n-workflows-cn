# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-06-17

### Added

- 1480 个 n8n 工作流模板，覆盖 6 大分类、60+ 细分场景
- 每个工作流标配 `workflow.json`（可导入 n8n）+ `readme.md`（中文说明与节点清单）
- `_cn_meta` 元数据标准：记录中文标题、分类、适配等级、来源 ID、同步时间
- 三级适配体系（Tier A/B/C），标注每个工作流的可用程度
- 14 项海外服务 → 国内服务替换方案（OpenAI→DeepSeek、Slack→飞书、Gmail→QQ邮箱 等）
- GitHub Pages 可搜索工作流浏览站点（暗色主题、分类筛选、关键词搜索）
- `INDEX.md` 完整索引（48 子分类折叠面板 + 中文功能描述）
- `CURATED.md` 精选合集（按场景分类的推荐工作流组合）
- `UPGRADE_GUIDE.md` Tier B→A 升级指南（21 个工作流的逐节点替换方案）
- `CONTRIBUTING.md` 贡献指南（Commit 规范、PR 流程、分支策略）
- `scripts/validate.py` 自动化验证脚本（JSON 格式、_cn_meta 完整性、目录结构）
- `scripts/build_index.py` INDEX.md 自动生成脚本
- `scripts/build_site.py` GitHub Pages 站点自动构建脚本
- GitHub Actions CI/CD：自动验证工作流合法性 + INDEX.md 可重建性检查

### Changed

- 统一 Tier 体系：去除 `A-adapted` / `B-adapted` / `C-adapted` 变体，归一为 A / B / C 三级
- 优化 README 结构：产品化改写、分类细化、徽章体系
