## 简介
**Generate Videos from Chat with Google Vertex AI (Veo3)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7954

---

# Generate Videos from Chat with Google Vertex AI (Veo3)


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| Poll for Video | HTTP Request |
| Edit Fields | 数据设置 |
| Convert to File | 转换为文件 |
| Post Veo3 Fast | HTTP Request |
| If | IF 判断 |
| Wait1 | 等待 |
| When chat message received | Chat 触发器 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
