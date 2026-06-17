## 简介
**Monitor website performance with Google PageSpeed, Sheets and multi-channel alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13009

---

# Monitor website performance with Google PageSpeed, Sheets and multi-channel alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get Data Form Sheet | Google Sheets |
| PageSpeed Test | HTTP Request |
| Save Results | Google Sheets |
| Process Results | Code |
| Update data | Google Sheets |
| Loop Over Items | 分批处理 |
| If3 | IF 判断 |
| PageSpeed Test2 | HTTP Request |
| Send a message | Discord |
| Rapiwa | rapiwa |
| Send a message2 | Email 发送 |
| Code (Calculate Days) | Code |
| Limit (10) | 数据限制 |
| If (check empty response) | IF 判断 |
| Wait 10s | 等待 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
