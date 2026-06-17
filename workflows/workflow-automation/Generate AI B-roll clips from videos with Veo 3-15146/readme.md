## 简介
**Generate AI B-roll clips from videos with Veo 3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15146

---

# Generate AI B-roll clips from videos with Veo 3


## 节点清单

| 节点 | 类型 |
|------|------|
| Set API Credentials | 数据设置 |
| Generate JWT Token | jwt |
| Request OAuth Token | HTTP Request |
| Extract Data from File | 从文件提取 |
| Post Video for Analysis | HTTP Request |
| Select Key Moments with AI | OpenAI |
| Split Moments into Items | Code |
| Batch Process Items | 分批处理 |
| Route Based on Status | Switch 路由 |
| Post to Video Generation API | HTTP Request |
| Post to Check Status API | HTTP Request |
| Wait 20 Seconds | 等待 |
| Convert Data to File | 转换为文件 |
| Upload File to GCS | googleCloudStorage |
| Set Unique File Name | 数据设置 |
| Set Project Details | 数据设置 |
| Generate JWT for Video | jwt |
| Request OAuth Token Again | HTTP Request |
| Aggregate Results | 数据聚合 |
| AI B-Roll Selector | OpenAI |
| Send Telegram Message | Telegram |
| Manual Trigger | 手动触发 |
| Set Video URL | 数据设置 |
| Fetch Video from URL | HTTP Request |
| Prepare Analysis Prompt | Code |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：17
- 输出节点：7
- 分类：workflow-automation
