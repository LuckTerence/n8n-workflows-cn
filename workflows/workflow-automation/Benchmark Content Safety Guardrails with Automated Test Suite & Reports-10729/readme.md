## 简介
**Benchmark Content Safety Guardrails with Automated Test Suite & Reports**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10729

---

# Benchmark Content Safety Guardrails with Automated Test Suite & Reports


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| OpenAI Chat Model | OpenAI Chat Model |
| Check Guardrails | guardrails |
| Format Pass Result | Code |
| Format Fail Result | Code |
| Combine Result | 数据合并 |
| Calculate Metrics | Code |
| Format Report | Code |
| Preserve Original Data | Code |
| Send a message | Email 发送 |
| Set Test Data (code) | Code |
| Markdown | Markdown |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
