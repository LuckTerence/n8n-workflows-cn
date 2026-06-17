## 简介
**Control SwitchBot devices via chat with OpenRouter AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15566

---

# Control SwitchBot devices via chat with OpenRouter AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Auth | Code |
| When chat message received | Chat 触发器 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Set Credentials | 数据设置 |
| Get Device List | HTTP Request |
| Generate API Request with AI | AI Agent |
| Send Device Command | HTTP Request |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
