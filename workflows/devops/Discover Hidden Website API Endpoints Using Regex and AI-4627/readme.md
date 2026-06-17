# Discover Hidden Website API Endpoints Using Regex and AI

https://n8nworkflows.xyz/workflows/4627

## 节点清单

| 节点 | 类型 |
|------|------|
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Start API Discovery | 手动触发 |
| Configuration | 数据设置 |
| Fetch Website HTML | HTTP Request |
| Extract URLs of JS files | HTML |
| Split URLs of JS files | 数据拆分 |
| Keep Relevant JS Files | 过滤器 |
| Fetch JS Content | HTTP Request |
| Extract API Endpoints | 数据设置 |
| Check Endpoints Count | IF 判断 |
| Split Endpoints | 数据拆分 |
| Remove Duplicates | 去重 |
| AI Endpoints Analysis | HTTP Request |
| Add Source Metadata | 数据设置 |
| Reference for Source Metadata | 空操作 |
| Process Each Analyzed File | 分批处理 |
| Format AI Results | 数据设置 |
| Prepare Endpoints File(s) | 转换为文件 |
| Save Endpoints File(s) | 读写文件 |
| Pass File Name, No Binary | 数据设置 |
| Merge AI Analysis & File Name | 数据合并 |
| Create Endpoints Regex With AI | AI Agent |
| Regex Generation LLM | OpenRouter Chat Model |
| Validate LLM Regex | 工作流工具 |
| Parse AI Regex Output | 结构化输出解析器 |
| Regex Validation Start | 执行工作流触发器 |
| Load Reference Endpoints | 读写文件 |
| Extract Endpoints File Text | 从文件提取 |
| Merge Regex, File Name & Reference Endpoints | 数据合并 |
| Evaluate LLM Regex | 数据设置 |
| Merge Initial AI Analysis & AI Agent Output | 数据合并 |
| Prepare Data for Regex Extraction | 数据设置 |
| Execute LLM Regex | 数据设置 |
| Split LLM-extracted Endpoints | 数据拆分 |
| Remove LLM Endpoints Duplicates | 去重 |
| Merge Original And LLM Endpoints | 数据合并 |
| Final Merge with Enriched File Name | 数据合并 |
| Sort Merged Endpoints | 数据排序 |
| Reorder Output Fields | 数据设置 |
| Export Comparison Results To Excel | 转换为文件 |
| Prepare Source & File Name for Merge | 去重 |
| Insufficient Endpoints | 空操作 |

## 触发方式
- Start API Discovery 触发
- Regex Validation Start 触发

## 统计
- 节点总数：42
- 触发节点：2
- 处理节点：37
- 输出节点：3
- 分类：devops
