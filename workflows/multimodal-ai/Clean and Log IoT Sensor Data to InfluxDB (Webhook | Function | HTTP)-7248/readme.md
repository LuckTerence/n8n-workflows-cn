## 简介
**Clean and Log IoT Sensor Data to InfluxDB (Webhook | Function | HTTP)**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7248

---

# Clean and Log IoT Sensor Data to InfluxDB (Webhook | Function | HTTP)


## 节点清单

| 节点 | 类型 |
|------|------|
| Sensor Input | Webhook |
| Clean & Transform Data | Function |
| Set Config | 数据设置 |
| HTTP Request | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图，Webhook 触发。

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

- 节点总数：4
- 触发方式：Webhook 触发

## 触发方式
- Sensor Input 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：multimodal-ai
