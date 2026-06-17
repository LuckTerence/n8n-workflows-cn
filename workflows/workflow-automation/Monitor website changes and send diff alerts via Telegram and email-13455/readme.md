## 简介
**Monitor website changes and send diff alerts via Telegram and email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13455

---

# Monitor website changes and send diff alerts via Telegram and email


## 节点清单

| 节点 | 类型 |
|------|------|
| ⏰ Every 4 Hours | 定时触发器 |
| 📋 URL List | Code |
| 🌐 Fetch Page | HTTP Request |
| 📄 Extract Content | Code |
| 📋 Load Previous Snapshot | Google Sheets |
| 🔍 Diff Engine | Code |
| 🔄 Changed? | IF 判断 |
| 💾 Save Snapshot | Google Sheets |
| 📲 Telegram Alert | Telegram |
| 📧 Email Alert | Email 发送 |
| 💾 Save (No Change) | Google Sheets |
| 📝 Log Result | Code |

## 触发方式
- ⏰ Every 4 Hours 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
