## 简介
**Automated Zalo OA Token Management with OAuth and Webhook Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8675

---

# Automated Zalo OA Token Management with OAuth and Webhook Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Store to SD & Pass token | Code |
| Refresh Token (Zalo v4) | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Execute_Node | Webhook |
| Clean Zalo Static Data | Code |
| Set Refresh Token and App ID | 数据设置 |
| Load to Static Data | Code |
| Webhook | Webhook |
| Load Access Token | Code |



## 功能说明

Automated Zalo OA Token Management with OAuth and。

定时触发、Webhook触发，通过 HTTP API 实现自动化。

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
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Schedule Trigger 触发
- Execute_Node 触发
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：3
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
