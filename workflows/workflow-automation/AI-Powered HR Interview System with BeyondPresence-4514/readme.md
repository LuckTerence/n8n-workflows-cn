## 简介
**AI-Powered HR Interview System with BeyondPresence**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4514

---

# AI-Powered HR Interview System with BeyondPresence


## 节点清单

| 节点 | 类型 |
|------|------|
| 📝 Your Job Description | Code |
| ▶️ Click to Start Setup | 手动触发 |
| Prepare Interview Agent | Code |
| Create Interview Agent | beyondPresence |
| Save Agent Info | Code |
| Receive Interview Data | Webhook |
| Confirm Receipt | 响应 Webhook |
| Is Our Interview? | IF 判断 |
| Analyze Interview | OpenAI |
| Format for Sheets | Code |
| Save to Google Sheets | Google Sheets |
| Data checks | Code |
| Save to Google Sheets1 | Google Sheets |

## 触发方式
- ▶️ Click to Start Setup 触发
- Receive Interview Data 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
