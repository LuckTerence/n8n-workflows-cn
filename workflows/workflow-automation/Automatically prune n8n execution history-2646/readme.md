## 简介
**Automatically prune n8n execution history**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/2646

---

# Automatically prune n8n execution history


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| n8n1 | n8n |
| n8n list execution | n8n |
| If | IF 判断 |
| Schedule Trigger | 定时触发器 |
| delete execution | n8n |
| No Operation, do nothing | 空操作 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
