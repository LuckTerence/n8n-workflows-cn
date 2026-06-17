## 简介
**Auto Germany Apartment Search & Apply with Immobilienscout24 & Google Services**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6150

---

# Auto Germany Apartment Search & Apply with Immobilienscout24 & Google Services


## 节点清单

| 节点 | 类型 |
|------|------|
| Cron Trigger | 定时触发器 |
| Set Config | 数据设置 |
| GeoID Lookup | Function |
| Fetch Listings From immobilienscout24 | HTTP Request |
| Filter Results | Function |
| Process Apartments One-by-One | 分批处理 |
| Fetch Schufa (Google Drive) | Google Drive |
| Fetch Salary Slips (Google Drive) | Google Drive |
| Generate Cover Letter | Function |
| Send Application Email | Email 发送 |
| Log to Google Sheet | Google Sheets |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- Cron Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
