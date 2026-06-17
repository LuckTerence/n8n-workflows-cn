## 简介
**Prevent simultaneous workflow executions with Redis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2270

---

# Prevent simultaneous workflow executions with Redis


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute Workflow | 执行工作流 |
| Schedule Trigger | 定时触发器 |
| Get Status | Redis |
| Set Running | Redis |
| Set Idle | Redis |
| Continue if Idle | 过滤器 |
| Redis Key exists | IF 判断 |
| No Operation | 空操作 |
| When clicking "Test workflow" | 手动触发 |
| Reset to Idle | Redis |

## 触发方式
- Schedule Trigger 触发
- When clicking "Test workflow" 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
