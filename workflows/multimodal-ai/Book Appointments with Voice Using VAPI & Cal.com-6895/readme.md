## 简介
**Book Appointments with Voice Using VAPI & Cal.com**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6895

---

# Book Appointments with Voice Using VAPI & Cal.com


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Switch | Switch 路由 |
| Set Variables | 数据设置 |
| Check Availability | HTTP Request |
| Book Appointment | HTTP Request |
| Booking SuccessFul | 响应 Webhook |
| Check Availability successful | 响应 Webhook |
| Prepare Payload Fields | 数据设置 |
| Extract Start & End Time | 数据设置 |



## 功能说明

AI 语音处理工作流，语音合成或转录，Webhook 触发。

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
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：multimodal-ai
