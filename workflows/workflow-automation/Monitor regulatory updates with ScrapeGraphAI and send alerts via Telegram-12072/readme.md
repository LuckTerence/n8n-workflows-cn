## 简介
**Monitor regulatory updates with ScrapeGraphAI and send alerts via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12072

---

# Monitor regulatory updates with ScrapeGraphAI and send alerts via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow | 手动触发 |
| Define Sources | Code |
| Split Sources | 分批处理 |
| Scrape Regulatory Data | ScrapeGraph AI |
| Merge Results | 数据合并 |
| Format & Deduplicate | Code |
| New Important Update? | IF 判断 |
| Prepare Telegram Message | 数据设置 |
| Send Telegram Alert | Telegram |
| Save to Redis | Redis |
| Error Handler | Code |

## 触发方式
- Start Workflow 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
