## 简介
**Extract University Term Dates from Excel using CloudFlare Markdown Conversion**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3505

---

# Extract University Term Dates from Excel using CloudFlare Markdown Conversion


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get Term Dates Excel | HTTP Request |
| Extract Key Events and Dates | 信息提取器 |
| Extract Target Sheet | 数据设置 |
| Fix Dates | 数据设置 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Create ICS File | 转换为文件 |
| Events to ICS Document | Code |
| Sort Events by Date | 数据排序 |
| Markdown Conversion Service | HTTP Request |
| Events to Items | 数据拆分 |
| Send Email with Attachment | Email 发送 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
