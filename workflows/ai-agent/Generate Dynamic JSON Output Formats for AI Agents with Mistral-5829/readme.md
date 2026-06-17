## 简介
**Generate Dynamic JSON Output Formats for AI Agents with Mistral**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5829

---

# Generate Dynamic JSON Output Formats for AI Agents with Mistral


## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Cloud Chat Model | Mistral Chat Model |
| JSON Output Parser | 结构化输出解析器 |
| JSON Generator | AI Agent |
| JSON Validator | AI Agent |
| JSON Output Parser 2 | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Prepare Input | 数据设置 |
| Loop Until it Works | 分批处理 |
| Update Input | 数据设置 |
| If Valid JSON | IF 判断 |
| JSON Reviewer | AI Agent |
| Guarantee Input | 数据设置 |
| Mistral Cloud Chat Model 2 | Mistral Chat Model |
| Advanced JSON Output Parser | advancedOutputParser |
| Update Input 2 | 数据设置 |
| JSON Format Works! | 空操作 |
| Prepare Output | 数据设置 |
| If No More Rounds | IF 判断 |
| Round Limit Reached | 停止并报错 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：18
- 输出节点：0
- 分类：ai-agent
