## 简介
**Personalized Outreach from Customer Emails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8968

---

# Personalized Outreach from Customer Emails


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Variables | 数据设置 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Create Draft Email For Review | Email 发送 |
| Generate Sales Email | 信息提取器 |
| Analyse and Build Persona | 信息提取器 |
| Get All Customer's Correspondence | Email 发送 |
| Get Contacts | hubspot |
| For Each Contact | 分批处理 |
| Contact Ref | 空操作 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
