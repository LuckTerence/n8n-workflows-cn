## 简介
**Extract personal data with self-hosted LLM Mistral NeMo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2766

---

# Extract personal data with self-hosted LLM Mistral NeMo


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Ollama Chat Model | Ollama Chat Model |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Structured Output Parser | 结构化输出解析器 |
| Basic LLM Chain | LLM Chain |
| On Error | 空操作 |
| Extract JSON Output | 数据设置 |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
