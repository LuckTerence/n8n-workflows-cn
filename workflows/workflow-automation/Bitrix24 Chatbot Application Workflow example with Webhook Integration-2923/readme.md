## 简介
**Bitrix24 Chatbot Application Workflow example with Webhook Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2923

---

# Bitrix24 Chatbot Application Workflow example with Webhook Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Bitrix24 Handler | Webhook |
| Credentials | 数据设置 |
| Validate Token | IF 判断 |
| Route Event | Switch 路由 |
| Process Message | Function |
| Process Join | Function |
| Process Install | Function |
| Register Bot | HTTP Request |
| Send Message | HTTP Request |
| Send Join Message | HTTP Request |
| Process Delete | 空操作 |
| Success Response | 响应 Webhook |
| Error Response | 响应 Webhook |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复，Webhook 触发。

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

- 节点总数：13
- 触发方式：Webhook 触发

## 触发方式
- Bitrix24 Handler 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
