## 简介
**Automate ASMR Video Creation and Distribution with FalAI and Social Media Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：18 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/5553

---

# Automate ASMR Video Creation and Distribution with FalAI and Social Media Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate Video | HTTP Request |
| Get Result | HTTP Request |
| Result | 数据设置 |
| Get Past Objects | Google Sheets |
| Prompt Agent | AI Agent |
| Idea Agent | AI Agent |
| Aggregate | 数据聚合 |
| Set Object List | 数据设置 |
| YouTube | HTTP Request |
| TikTok | HTTP Request |
| Instagram | HTTP Request |
| Delete First Row | Google Sheets |
| Append Object | Google Sheets |
| Object & Caption | 结构化输出解析器 |
| Upload | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| When clicking ‘Execute workflow’ | 手动触发 |
| 1 Minute - Video taking longer please wait | 等待 |
| 5 Minutes - Wait for Video | 等待 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
