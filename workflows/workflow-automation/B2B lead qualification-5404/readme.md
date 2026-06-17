## 简介
**B2B lead qualification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5404

---

# B2B lead qualification


## 节点清单

| 节点 | 类型 |
|------|------|
| New Lead Captured | Google Sheets 触发器 |
| Initiate Voice Call (VAPI) | HTTP Request |
| Save Qualified Lead to CRM Sheet | Google Sheets |
| Send Call Data Acknowledgement | 响应 Webhook |
| Receive Lead Details from VAPI | Webhook |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：Webhook 触发

## 触发方式
- New Lead Captured 触发
- Receive Lead Details from VAPI 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：1
- 输出节点：2
- 分类：workflow-automation
