## 简介
**Daily Podcast Summary**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2433

---

# Daily Podcast Summary


## 节点清单

| 节点 | 类型 |
|------|------|
| Gmail | Email 发送 |
| TaddyTopDaily | HTTP Request |
| Genre | 数据设置 |
| Split Out | 数据拆分 |
| Whisper Transcribe Audio | HTTP Request |
| Final Data | 数据设置 |
| Merge Results | Code |
| HTML | HTML |
| Summarize Podcast | OpenAI |
| Schedule | 定时触发器 |
| Request Audio Crop | HTTP Request |
| Get Download Link | HTTP Request |
| Download Cut MP3 | HTTP Request |
| Download Podcast | HTTP Request |
| Wait | 等待 |
| If Downloads Ready | IF 判断 |

## 触发方式
- Schedule 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：8
- 输出节点：7
- 分类：workflow-automation
