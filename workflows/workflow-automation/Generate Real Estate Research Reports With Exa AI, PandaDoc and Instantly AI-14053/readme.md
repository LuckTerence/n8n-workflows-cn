## 简介
**Generate Real Estate Research Reports With Exa AI, PandaDoc and Instantly AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：19
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
