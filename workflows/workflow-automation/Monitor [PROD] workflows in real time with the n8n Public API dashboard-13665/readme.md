## 简介
**Monitor [PROD] workflows in real time with the n8n Public API dashboard**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13665

---

# Monitor [PROD] workflows in real time with the n8n Public API dashboard


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| Respond to Webhook | 响应 Webhook |
| Webhook | Webhook |
| GET success | HTTP Request |
| GET error | HTTP Request |
| Compare | Code |
| HTML | Code |
| Config | 数据设置 |
| API: List Workflows | HTTP Request |
| Filter: [PROD] Tag | Code |



## 功能说明

监控告警系统，异常检测并发送通知，Webhook 触发。

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

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
