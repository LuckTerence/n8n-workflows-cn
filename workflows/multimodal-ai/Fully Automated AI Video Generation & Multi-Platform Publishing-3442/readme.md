## 简介
**Fully Automated AI Video Generation & Multi-Platform Publishing**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3442

---

# Fully Automated AI Video Generation & Multi-Platform Publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| Get image | HTTP Request |
| Generate Image | HTTP Request |
| Image-to-Video | HTTP Request |
| Get Video | HTTP Request |
| List Elements | Code |
| Wait 10min | 等待 |
| Wait 3min | 等待 |
| Wait 5min | 等待 |
| Generate voice | HTTP Request |
| List Elements1 | Code |
| Fail check | IF 判断 |
| Wait to retry | 等待 |
| Generate Image Prompts | OpenAI |
| Calculate Token Usage | Code |
| Check for failures | IF 判断 |
| Generate Video Captions | OpenAI |
| Match captions with videos | 数据合并 |
| Generate Script | OpenAI |
| Upload Voice Audio | Google Drive |
| Set Access Permissions | Google Drive |
| Pair Videos with Audio | 数据合并 |
| Render Final Video | HTTP Request |
| Notify me on Discord | Discord |
| Once Per Day | 定时触发器 |
| Load Google Sheet | Google Sheets |
| Create List | Code |
| Wait1 | 等待 |
| Get Final Video | HTTP Request |
| Upload Final Video | Google Drive |
| Get Raw File | HTTP Request |
| Set Permissions | Google Drive |
| Update Google Sheet | Google Sheets |
| Set API Keys | 数据设置 |
| Validate list formatting | IF 判断 |
| Get Audio from Video | OpenAI |
| Generate Description for Videos  in Tiktok and Instagram | OpenAI |
| Upload Video and Description to Tiktok | HTTP Request |
| Upload Video and Description to Instagram | HTTP Request |
| Upload Video and Description to Youtube | HTTP Request |
| Upload Video and Description to Facebook | HTTP Request |
| Upload Video and Description to Linkedin | HTTP Request |
| Read Video from Google Drive | 读取二进制文件 |
| Write video | 写入二进制文件 |

## 触发方式
- Once Per Day 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：28
- 输出节点：14
- 分类：multimodal-ai
