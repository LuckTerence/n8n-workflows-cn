## 简介
**Bulk Auto-Publish Videos to Social Networks with AI Copy and Client Approval**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11638

---

# Bulk Auto-Publish Videos to Social Networks with AI Copy and Client Approval


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Campaign | 表单触发器 |
| Campaign Settings | 数据设置 |
| Fetch Videos from Drive | Google Drive |
| Video Files Only | 过滤器 |
| Build Schedule Calendar | Code |
| Process Each Video | 分批处理 |
| Download from Drive | Google Drive |
| AI Video Analysis | OpenAI Chat Model |
| Generate Social Copy | AI Agent |
| Gemini Pro | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Format Content Data | Code |
| Save Draft to Sheet | Google Sheets |
| Publisher Config | 数据设置 |
| Load Content Queue | Google Sheets |
| Only Approved | 过滤器 |
| Process Queue | 分批处理 |
| Get Video File | Google Drive |
| Build Upload Payload | Code |
| TikTok Enabled? | IF 判断 |
| Instagram Enabled? | IF 判断 |
| YouTube Enabled? | IF 判断 |
| Schedule TikTok | uploadPost |
| Schedule Instagram | uploadPost |
| Schedule YouTube | uploadPost |
| Mark as Scheduled | Google Sheets |
| 15 mins check | 定时触发器 |



## 功能说明

AI 视频生成工作流，自动创作视频内容，定时执行（Bulk)表单提交触发、定时触发，通过 HTTP API 实现自动化。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：表单提交触发, 定时触发

## 触发方式
- Start Campaign 触发
- 15 mins check 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：25
- 输出节点：0
- 分类：workflow-automation
