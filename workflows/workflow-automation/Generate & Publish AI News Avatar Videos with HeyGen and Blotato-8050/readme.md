## 简介
**Generate & Publish AI News Avatar Videos with HeyGen and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8050

---

# Generate & Publish AI News Avatar Videos with HeyGen and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload to Blotato1 | HTTP Request |
| Schedule Trigger1 | 定时触发器 |
| AI Agent1 | AI Agent |
| Wait6 | 等待 |
| Write Script1 | OpenAI Chat Model |
| Setup Heygen1 | 数据设置 |
| Get Avatar Video1 | HTTP Request |
| Prepare for Publish1 | 数据设置 |
| Write Long Caption1 | OpenAI |
| Write Short Caption1 | OpenAI |
| Create Avatar Video1 | HTTP Request |
| Write Title1 | OpenAI |
| [TikTOK] Publish via Blotato1 | HTTP Request |
| [TikTOK] Publish via Blotato | HTTP Request |
| [TikTOK] Publish via Blotato2 | HTTP Request |
| [TikTOK] Publish via Blotato3 | HTTP Request |
| [TikTOK] Publish via Blotato4 | HTTP Request |
| [TikTOK] Publish via Blotato5 | HTTP Request |
| [TikTOK] Publish via Blotato6 | HTTP Request |
| [TikTOK] Publish via Blotato7 | HTTP Request |
| Read AI News Feed | rssFeedReadTool |
| Read AI News Feed1 | rssFeedReadTool |

## 触发方式
- Schedule Trigger1 触发
- Read AI News Feed 触发
- Read AI News Feed1 触发

## 统计
- 节点总数：22
- 触发节点：3
- 处理节点：8
- 输出节点：11
- 分类：workflow-automation
