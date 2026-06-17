## 简介
**Meta Ads Daily Report to Google Sheet and Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5125

---

# Meta Ads Daily Report to Google Sheet and Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Ads Data | HTTP Request |
| Set Yesterday's Date	 | 数据设置 |
| Trigger - Daily at 9AM	 | 定时触发器 |
| Transform Ads Data	 | Code |
| Update Google Sheet	 | Google Sheets |
| Generate Email HTML	 | Code |
| Send Email Report	 | Email 发送 |

## 触发方式
- Trigger - Daily at 9AM	 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
