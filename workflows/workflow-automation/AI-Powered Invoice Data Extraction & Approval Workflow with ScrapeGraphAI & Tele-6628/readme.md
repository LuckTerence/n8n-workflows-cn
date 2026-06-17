## 简介
**AI-Powered Invoice Data Extraction & Approval Workflow with ScrapeGraphAI & Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/6628

---

# AI-Powered Invoice Data Extraction & Approval Workflow with ScrapeGraphAI & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger | Email 读取 |
| File Upload Webhook | Webhook |
| File Processor | Code |
| ScrapeGraphAI - Invoice Extractor | ScrapeGraph AI |
| Data Extractor & Cleaner | Code |
| Validation Rules Engine | Code |
| Approval Required? | Switch 路由 |
| Approval Workflow Generator | Code |
| Approval Notification | Telegram |
| Accounting System Integration | HTTP Request |

## 触发方式
- File Upload Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
