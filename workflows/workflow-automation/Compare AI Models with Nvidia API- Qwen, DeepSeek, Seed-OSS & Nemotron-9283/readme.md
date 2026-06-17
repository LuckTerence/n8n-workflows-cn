## 简介
**Compare AI Models with Nvidia API: Qwen, DeepSeek, Seed-OSS & Nemotron**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9283

---

# Compare AI Models with Nvidia API: Qwen, DeepSeek, Seed-OSS & Nemotron


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Format Response | 数据设置 |
| Send Aggregated AI Model Responses | 响应 Webhook |
| Merge AI Model | 数据合并 |
| AI Model Router | Switch 路由 |
| Query Qwen3-next-80b-a3b-thinking (Alibaba) | HTTP Request |
| Query Bytedance/seed-oss-36b-instruct (Bytedance) | HTTP Request |
| Query Nvidia-nemotron-nano-9b-v2 (Nvidia) | HTTP Request |
| Query DeepSeekv3_1 | HTTP Request |



## 功能说明

API 集成接口，连接和编排多个第三方服务，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：3
- 输出节点：5
- 分类：workflow-automation
