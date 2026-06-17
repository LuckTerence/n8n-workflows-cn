## 简介
**Generate merchandise proposals and market research from NASA APOD**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11291

---

# Generate merchandise proposals and market research from NASA APOD


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger1 | 定时触发器 |
| Workflow Configuration1 | 数据设置 |
| Get NASA APOD1 | nasa |
| Generate Keywords & Check Logo1 | OpenAI |
| Create Mockup with Cloudinary1 | HTTP Request |
| Search Etsy Market1 | apify |
| Calculate Profit1 | Code |
| Merge Data1 | 数据合并 |
| AI Marketing Advisor1 | OpenAI |
| Send Slack Proposal1 | Slack |
| Wait for User Decision1 | 等待 |
| Check User Decision1 | Switch 路由 |
| Download NASA Image1 | HTTP Request |
| Save to Google Drive1 | Google Drive |
| Save to Notion DB1 | Notion |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，定时执行。

定时触发，通过 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：15
- 触发方式：定时触发

## 触发方式
- Schedule Trigger1 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
