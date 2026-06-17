# Generate Creative Solutions with Dual AI Agents, Randomization & Redis

https://n8nworkflows.xyz/workflows/8383

## 节点清单

| 节点 | 类型 |
|------|------|
| Random Word Generator | AI Agent |
| mersenne_twister | Code |
| store_idea | Redis |
| count_ideas | Redis |
| get_count | Redis |
| check_queue_is_empty | IF 判断 |
| extract_ideas | Redis |
| get_idea | Redis |
| set_idea | Redis |
| Brainstorming | AI Agent |
| chat | Chat 触发器 |
| OpenAI Chat Model - Critic | OpenAI Chat Model |
| check_number_of_ideas | IF 判断 |
| filtering | 数据设置 |
| get_random_number | 数据设置 |
| Critic | AI Agent |
| OpenAI Chat Model - Word Generator | OpenAI Chat Model |
| Google Gemini Chat Model - Brainstorming | OpenAI Chat Model |

## 触发方式
- chat 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：17
- 输出节点：0
- 分类：ai-agent
