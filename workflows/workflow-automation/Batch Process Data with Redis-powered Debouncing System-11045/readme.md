## 简介
**Batch Process Data with Redis-powered Debouncing System**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11045

---

# Batch Process Data with Redis-powered Debouncing System


## 节点清单

| 节点 | 类型 |
|------|------|
| Crypto | 加密 |
| Set last update uuid | Redis |
| Push to message list | Redis |
| Get last update uuid | Redis |
| Am I last? | IF 判断 |
| Set lock | Redis |
| Get messages | Redis |
| Clear messages | Redis |
| Release lock | Redis |
| Get lock value | Redis |
| Is lock active? | IF 判断 |
| Wait for lock release | 等待 |
| Split messages | 数据拆分 |
| Trigger | 执行工作流触发器 |
| Wait | 等待 |

## 触发方式
- Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
