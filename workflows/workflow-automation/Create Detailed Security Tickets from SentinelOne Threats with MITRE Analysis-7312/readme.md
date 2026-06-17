## 简介
**Create Detailed Security Tickets from SentinelOne Threats with MITRE Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7312

---

# Create Detailed Security Tickets from SentinelOne Threats with MITRE Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| New SentinelOne Threat | Webhook |
| Extract Threat Intelligence | Code |
| Fetch Autotask Users | HTTP Request |
| Load Client Companies | HTTP Request |
| Process Company Data | 数据拆分 |
| Retrieve Ticket Fields | HTTP Request |
| Parse Field Options | Code |
| Map Client Company | Code |
| Create Security Ticket | HTTP Request |
| Rate Limit Delay 1 | 等待 |
| Rate Limit Delay 2 | 等待 |
| Wait | 等待 |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化，Webhook 触发。

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

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- New SentinelOne Threat 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
