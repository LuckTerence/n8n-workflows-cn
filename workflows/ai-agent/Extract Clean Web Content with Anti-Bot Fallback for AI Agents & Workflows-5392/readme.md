## 简介
**Extract Clean Web Content with Anti-Bot Fallback for AI Agents & Workflows**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5392

---

# Extract Clean Web Content with Anti-Bot Fallback for AI Agents & Workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| Content Extractor | webpageContentExtractor |
| Try Antibot Evasion | IF 判断 |
| Scrape.do | HTTP Request |
| Server Error | 停止并报错 |
| Not 404 | IF 判断 |
| Not Found | 停止并报错 |
| Simple Scraper | HTTP Request |
| Full Text | IF 判断 |
| Fulltext Output | 数据设置 |
| Summary Output | 数据设置 |
| Is Binary | IF 判断 |
| ContentType Error | 停止并报错 |
| Workflow Call | 执行工作流触发器 |

## 触发方式
- Workflow Call 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：ai-agent
