## 简介
**Generate Animal Battle Videos with Flux AI, Creatomate & Multi-Platform Publishing**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：33 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10735

---

# Generate Animal Battle Videos with Flux AI, Creatomate & Multi-Platform Publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| Render Video | HTTP Request |
| Get Main Character | Google Sheets |
| Scene Creator | AI Agent |
| GPT 4.1-mini | OpenRouter Chat Model |
| Image Prompt Generator | AI Agent |
| Split Out | 数据拆分 |
| Main Character | 数据设置 |
| Merge | 数据合并 |
| Opponents | 数据设置 |
| Scenes | 结构化输出解析器 |
| Close Ups | 结构化输出解析器 |
| Winner Image Prompt | AI Agent |
| Get Video | HTTP Request |
| Generate Close Ups | HTTP Request |
| Split Out1 | 数据拆分 |
| 90 seconds | 等待 |
| Get Close Ups | HTTP Request |
| Add Close Ups | Google Sheets |
| Aggregate | 数据聚合 |
| Generate Scene | HTTP Request |
| Get Winners | HTTP Request |
| 90_seconds | 等待 |
| GPT 4.1 | OpenRouter Chat Model |
| Aggregate1 | 数据聚合 |
| Add Winner | Google Sheets |
| Merge1 | 数据合并 |
| Get Elements | Google Sheets |
| Google Sheets | Google Sheets |
| 90_Seconds | 等待 |
| Upload to Blotato | HTTP Request |
| Instagram | HTTP Request |
| TikTok | HTTP Request |
| YouTube | HTTP Request |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：34
- 触发节点：1
- 处理节点：23
- 输出节点：10
- 分类：multimodal-ai
