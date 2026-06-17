## 简介
**Simulate Debates Between AI Agents Using Mistral to Optimize Answers**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5682

---

# Simulate Debates Between AI Agents Using Mistral to Optimize Answers


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule | 定时触发器 |
| Configure Workflow Args | globalConstants |
| When clicking ‘Execute workflow’ | 手动触发 |
| Email Trigger (IMAP) | Email 读取 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Simple Memory | 记忆缓冲区 |
| Prepare Input | 数据设置 |
| Update Input | 数据设置 |
| Split Out AI Agents | 数据拆分 |
| JSON Output Parser | 结构化输出解析器 |
| If No More Rounds | IF 判断 |
| End of Debate | 空操作 |
| Debate Loop | 分批处理 |
| Round Loop | 分批处理 |
| Debate Actor Abstraction | AI Agent |
| Debate Environment | AI Agent |
| Guarantee Input | 数据设置 |
| Mistral Cloud Chat Model 2 | Mistral Chat Model |
| Aggregate | 数据聚合 |
| JSON Output Parser 2 | 结构化输出解析器 |
| Simple Memory 2 | 记忆缓冲区 |
| Wait Before Sending Agents | 等待 |
| Wait 1 | 等待 |
| Wait 2 | 等待 |

## 触发方式
- Schedule 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：21
- 输出节点：1
- 分类：ai-agent
