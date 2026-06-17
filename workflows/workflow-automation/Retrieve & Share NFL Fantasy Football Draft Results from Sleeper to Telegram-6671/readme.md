## 简介
**Retrieve & Share NFL Fantasy Football Draft Results from Sleeper to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6671

---

# Retrieve & Share NFL Fantasy Football Draft Results from Sleeper to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract Username | Code |
| Get Sleeper User ID | HTTP Request |
| Send a text message | Telegram |
| Send Message to Chatbot | Telegram 触发器 |
| Get Drafts | HTTP Request |
| Extract Draft ID | Code |
| Get Draft Picks | HTTP Request |
| Return Picked By results from User ID w/ League year and format included | Code |

## 触发方式
- Send Message to Chatbot 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
