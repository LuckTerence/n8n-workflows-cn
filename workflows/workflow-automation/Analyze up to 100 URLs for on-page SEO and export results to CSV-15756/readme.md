## 简介
**Analyze up to 100 URLs for on-page SEO and export results to CSV**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15756

---

# Analyze up to 100 URLs for on-page SEO and export results to CSV


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Through URL Batches | 分批处理 |
| Fetch Page HTML Payload | HTTP Request |
| Verify HTTP 200 Status | IF 判断 |
| Inspect HTML Content Structure | Code |
| Validate HTML Compliance Status | IF 判断 |
| Receive Chat Message Input | Chat 触发器 |
| Extract and Normalize URLs | Code |
| Check Empty URL List | IF 判断 |
| Verify Maximum URL Limit | IF 判断 |
| Format URL JSON Objects | Code |
| Split Into Individual Items | 列表操作 |
| Check For Skipped Inputs | IF 判断 |
| Send Empty Input Error | 聊天 |
| Send Maximum Limit Error | 聊天 |
| Send Skipped Input Warning | 聊天 |
| Remove Duplicate Records | 去重 |
| Send Progress Update | 聊天 |
| Verify Processed URLs | IF 判断 |
| Loop Tag Extraction | 分批处理 |
| Aggregate Loop Data | 数据合并 |
| Format Final Dataset | 数据设置 |
| Generate CSV File | 转换为文件 |
| Upload to Server | HTTP Request |
| Extract Download URL | Code |
| Send Download Link | 聊天 |
| Extract Header Data | 数据设置 |
| Send Fetch Error | 聊天 |
| Map Failed Request Data | 数据设置 |
| Send Status Code Error | 聊天 |
| Map Status Error Data | 数据设置 |
| Map Compliance Error Data | 数据设置 |
| Format Valid Page Data | Code |
| Send Success URL Notification | 聊天 |
| Send Error URL | 聊天 |
| Extract SEO Tags | HTML |

## 触发方式
- Receive Chat Message Input 触发

## 统计
- 节点总数：35
- 触发节点：1
- 处理节点：23
- 输出节点：11
- 分类：workflow-automation
