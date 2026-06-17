## 简介
**Implement Recursive Algorithms with Sub-workflows: Towers of Hanoi Demo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8656

---

# Implement Recursive Algorithms with Sub-workflows: Towers of Hanoi Demo


## 节点清单

| 节点 | 类型 |
|------|------|
| Set number of discs | 数据设置 |
| Max 1 disc | IF 判断 |
| A B C | 执行工作流 |
| X Y Z | 执行工作流触发器 |
| X to Z | Code |
|  X to Z | Code |
| Update | Code |
|  Update | Code |
| Create stacks | Code |
| X Z Y | 执行工作流 |
| Y X Z | 执行工作流 |
| Solution | Code |
| Start | 手动触发 |

## 触发方式
- X Y Z 触发
- Start 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
