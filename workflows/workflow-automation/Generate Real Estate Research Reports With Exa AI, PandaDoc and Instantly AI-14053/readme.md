## 简介
**Generate Real Estate Research Reports With Exa AI, PandaDoc and Instantly AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14053

---

# Generate Real Estate Research Reports With Exa AI, PandaDoc and Instantly AI


## 节点清单

| 节点 | 类型 |
|------|------|
| If | IF 判断 |
| Wait | 等待 |
| HTTP Request | HTTP Request |
| Create a research task | exa |
| Get a research task | exa |
| If1 | IF 判断 |
| Wait1 | 等待 |
| PandaDoc (Generate Presentation) | HTTP Request |
| PandaDoc (checkPresentationStatus) | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Pending Approval | Slack |
| Batch Instantly Upload | 分批处理 |
| Instantly Add Lead | HTTP Request |
| Wait for Instantly Rate Limit | 等待 |
| Prep Batch Upload Data | Code |
| Update Sheet Status | Google Sheets |
| Aggregate Final Results | Code |
| Send a message1 | Slack |
| Fetch contact | Google Sheets |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
