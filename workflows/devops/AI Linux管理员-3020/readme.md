## 简介
**AI Linux管理员**

用AI管理Linux VPS实例

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3020

---

# AI Linux 管理员


通过 Webhook 接收管理指令，AI Agent 连接 SSH 在目标服务器上执行运维操作。

## 节点

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook 触发器 |
| AI Agent | AI Agent |
| SSH | SSH 连接 |
| Code | 数据处理 |
| Webhook Response | 响应输出 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

Chat 消息触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：Chat 消息触发

## 触发方式

HTTP Webhook 触发

## 统计

