## 简介
**Automate ASMR Glass Fruit Video Creation & Publishing with Veo, Shotstack & Postiz**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：28 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10175

---

# Automate ASMR Glass Fruit Video Creation & Publishing with Veo, Shotstack & Postiz


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Past Objects | Google Sheets |
| Prompt Agent | AI Agent |
| Idea Agent | AI Agent |
| Aggregate | 数据聚合 |
| Set Object List | 数据设置 |
| Object & Caption | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| OpenAI Chat Model | OpenAI Chat Model |
| SET | 数据设置 |
| JWT | jwt |
| GET TOKEN | HTTP Request |
| Switch | Switch 路由 |
| Generate Video | HTTP Request |
| Fetch Status | HTTP Request |
| Wait | 等待 |
| Convert to File | 转换为文件 |
| Rendering... | 等待 |
| Download final video | HTTP Request |
| Upload to GCS (To be accessible via URL) | googleCloudStorage |
| Turn video to 9:16 | HTTP Request |
| Done? | IF 判断 |
| Configure me | 数据设置 |
| Done?1 | HTTP Request |
| Upload video to Postiz | HTTP Request |
| Get Postiz integrations | HTTP Request |
| Switch1 | Switch 路由 |
| Schedule YouTube | HTTP Request |
| Schedule TikTok | HTTP Request |
| Schedule Instagram | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：17
- 输出节点：11
- 分类：workflow-automation
