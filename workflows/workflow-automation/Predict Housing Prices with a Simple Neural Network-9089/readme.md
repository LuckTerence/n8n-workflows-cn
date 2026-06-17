## 简介
**Predict Housing Prices with a Simple Neural Network**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9089

---

# Predict Housing Prices with a Simple Neural Network


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Number of Rooms | Code |
| Distance to City | Code |
| Age | Code |
| Square Feet | Code |
| Output Merge | 数据合并 |
| Respond to Webhook | 响应 Webhook |
| Merge 1 | 数据合并 |
| Merge 2 | 数据合并 |
| Neuron 1 - Input 1 - Weight | 数据设置 |
| Neuron 1 - Input 2- Weight | 数据设置 |
| Neuron 1 - Input 3 - Weight | 数据设置 |
| Neuron 1 - Input 4 - Weight | 数据设置 |
| Neuron 1 - Input 1 | 数据设置 |
| Neuron 1 - Input 2 | 数据设置 |
| Neuron 1 - Input 3 | 数据设置 |
| Neuron 1 - Input 4 | 数据设置 |
| Neuron 2 - Input 1 | 数据设置 |
| Neuron 2 - Input 2 | 数据设置 |
| Neuron 2 - Input 3 | 数据设置 |
| Neuron 1 - Weighted Sum | Code |
| Neuron 1 - Bias | 数据设置 |
| Neuron 2 - Input 1 - Weight | 数据设置 |
| Neuron 2 - Input 4 - Weight | 数据设置 |
| Neuron 2 - Weighted Sum | Code |
| Neuron 2 - Bias | 数据设置 |
| Neuron 1 - ReLU | 数据设置 |
| Neuron 2 - ReLU | 数据设置 |
| Neuron 2- Input 4 | 数据设置 |
| Neuron 2- Input 3 - Weight | 数据设置 |
| Neuron 2 - Input 2- Weight | 数据设置 |
| Output - Neuron 1 | 数据设置 |
| Output - Neuron 2 | 数据设置 |
| Output - Neuron 1 - Weight | 数据设置 |
| Output - Neuron 2 - Weight | 数据设置 |
| Output - Weighted Sum | Code |
| Output - Bias | 数据设置 |



## 功能说明

Predict Housing Prices with a Simple Neural Networ。

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

- 节点总数：37
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：37
- 触发节点：1
- 处理节点：35
- 输出节点：1
- 分类：workflow-automation
