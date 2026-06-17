## 简介
**Qualify insurance quote leads with Aloware SMS and AI voice agent**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15030

---

# Qualify insurance quote leads with Aloware SMS and AI voice agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Quote Request Received | Webhook |
| Normalize Quote Data | 数据设置 |
| Aloware: Create Contact with Quote Details | HTTP Request |
| Aloware: Send Quote Acknowledgment SMS | HTTP Request |
| Is Urgent Quote? | IF 判断 |
| Aloware: Enroll in AI Voice Agent Sequence | HTTP Request |
| Aloware: Enroll in Nurture Sequence | HTTP Request |



## 功能说明

AI 语音处理工作流，语音合成或转录，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：7
- 触发方式：Webhook 触发

## 触发方式
- Quote Request Received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：multimodal-ai
