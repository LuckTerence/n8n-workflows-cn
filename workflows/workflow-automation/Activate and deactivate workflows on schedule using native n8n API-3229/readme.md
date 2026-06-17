## 简介
**Activate and deactivate workflows on schedule using native n8n API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3229

---

# Activate and deactivate workflows on schedule using native n8n API


## 节点清单

| 节点 | 类型 |
|------|------|
| n8n Activate | n8n |
| n8n Deactivate | n8n |
| Workflow ID | 数据设置 |
| Merge in Workflow ID for deactivation | 数据合并 |
| Merge in Workflow ID for activation | 数据合并 |
| Activate at 08:00 daily | 定时触发器 |
| Deactivate at 20:00 daily | 定时触发器 |

## 触发方式
- Activate at 08:00 daily 触发
- Deactivate at 20:00 daily 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
