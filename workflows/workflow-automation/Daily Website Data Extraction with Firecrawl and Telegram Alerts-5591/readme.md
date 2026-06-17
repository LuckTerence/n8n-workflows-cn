## 简介
**Daily Website Data Extraction with Firecrawl and Telegram Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5591

---

# Daily Website Data Extraction with Firecrawl and Telegram Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract | HTTP Request |
| Get Results | HTTP Request |
| Edit Fields | 数据设置 |
| Schedule Trigger | 定时触发器 |
| If | IF 判断 |
| 30 Secs | 等待 |
| Wait 15 secs | 等待 |
| Telegram | Telegram |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
