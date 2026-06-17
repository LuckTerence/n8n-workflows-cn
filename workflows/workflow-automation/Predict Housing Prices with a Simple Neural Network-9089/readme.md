## 简介
**Predict Housing Prices with a Simple Neural Network**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：36 | 难度：⭐⭐⭐ 高级
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

## 触发方式
- Webhook 触发

## 统计
- 节点总数：37
- 触发节点：1
- 处理节点：35
- 输出节点：1
- 分类：workflow-automation
