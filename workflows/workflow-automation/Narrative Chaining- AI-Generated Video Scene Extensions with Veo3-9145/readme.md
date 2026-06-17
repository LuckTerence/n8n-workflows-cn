## 简介
**Narrative Chaining: AI-Generated Video Scene Extensions with Veo3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9145

---

# Narrative Chaining: AI-Generated Video Scene Extensions with Veo3


## 节点清单

| 节点 | 类型 |
|------|------|
| Think | 思考工具 |
| GPT | OpenAI Chat Model |
| Analyze Video | HTTP Request |
| Get Analysis | HTTP Request |
| Looper | 数据设置 |
| If | IF 判断 |
| Combine Clips | HTTP Request |
| Get Final Video | HTTP Request |
| Aggregate | 数据聚合 |
| Get input | Google Sheets |
| Initial Values | 数据设置 |
| Request last | HTTP Request |
| Get last | HTTP Request |
| Get Video | HTTP Request |
| Create Video | HTTP Request |
| Add scene | Google Sheets |
| Increment step | 数据设置 |
| If complete | IF 判断 |
| ExtendRobo AI Agent | AI Agent |
| Wait 2 | 等待 |
| Wait 1 | 等待 |
| Wait | 等待 |
| Get scenes | Google Sheets |
| Wait 3 | 等待 |
| Update log | Google Sheets |
| Structured Output | 结构化输出解析器 |
| Execute | 手动触发 |
| Clear scenes | Google Sheets |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：28
- 触发方式：手动触发

## 触发方式
- Execute 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：19
- 输出节点：8
- 分类：workflow-automation
