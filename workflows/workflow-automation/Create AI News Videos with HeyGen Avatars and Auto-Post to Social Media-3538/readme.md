## 简介
**Create AI News Videos with HeyGen Avatars and Auto-Post to Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：23 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/3538

---

# Create AI News Videos with HeyGen Avatars and Auto-Post to Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload to Blotato | HTTP Request |
| [Instagram] Publish via Blotato | HTTP Request |
| [Facebook] Publish via Blotato | HTTP Request |
| [Linkedin] Publish via Blotato | HTTP Request |
| [Tiktok] Publish via Blotato | HTTP Request |
| OpenAI | OpenAI |
| Upload to Blotato - Image | HTTP Request |
| [Pinterest] Publish via Blotato | HTTP Request |
| [Youtube] Publish via Blotato | HTTP Request |
| [Threads] Publish via Blotato | HTTP Request |
| [Twitter] Publish via Blotato | HTTP Request |
| [Bluesky] Publish via Blotato | HTTP Request |
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| Fetch HN Article | hackerNewsTool |
| Fetch HN Front Page | hackerNewsTool |
| Wait | 等待 |
| Write Script | OpenAI Chat Model |
| Setup Heygen | 数据设置 |
| Get Avatar Video | HTTP Request |
| Prepare for Publish | 数据设置 |
| Write Long Caption | OpenAI |
| Write Short Caption | OpenAI |
| Create Avatar Video | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：10
- 输出节点：13
- 分类：workflow-automation
