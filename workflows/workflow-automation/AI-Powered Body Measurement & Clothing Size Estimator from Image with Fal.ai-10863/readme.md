## 简介
**AI-Powered Body Measurement & Clothing Size Estimator from Image with Fal.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10863

---

# AI-Powered Body Measurement & Clothing Size Estimator from Image with Fal.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Get status | HTTP Request |
| Completed? | IF 判断 |
| Form | 表单 |
| Wait 10 sec. | 等待 |
| Send image to estimator | HTTP Request |
| Get result | HTTP Request |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Send a message | Email 发送 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |



## 功能说明

AI 图像生成工作流，文生图或图生图，Webhook 触发（Powered)表单提交触发、Webhook 触发，通过 邮箱 + HTTP API 实现自动化。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：表单提交触发, Webhook 触发

## 触发方式
- On form submission 触发
- Webhook 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
