## 简介
**Automated Email Blast with Follow-Ups & Response Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7175

---

# Automated Email Blast with Follow-Ups & Response Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger | 定时触发器 |
| Fetch Contact Data  | Google Sheets |
| Iterate Contacts | 分批处理 |
| Determine Follow-Up Stage | IF 判断 |
| Route by Follow-Up Stage | Switch 路由 |
| Send Follow-Up Email 1  | Email 发送 |
| Send Follow-Up Email 2 | Email 发送 |
| Update Sheet with Follow-Up Status | Google Sheets |
| Check Email Responses | Email 读取 |
| Update Sheet with Response  | Google Sheets |

## 触发方式
- Daily Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
