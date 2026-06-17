## 简介
**Audio Transcription with Telegram and Groq Whisper**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10037

---

# Audio Transcription with Telegram and Groq Whisper


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram: Receive Message | Telegram 触发器 |
| Switch (Check Message Type) | Switch 路由 |
| Telegram: Unsupported Type Message | Telegram |
| Set Node (audio type) | 数据设置 |
| Set Node (voice type) | 数据设置 |
| Telegram: Download Audio File | Telegram |
| HTTP - Transcribe Audio (Groq) | HTTP Request |
| Set Credentials (Groq + Telegram) | 数据设置 |
| Telegram: Send Output Options | Telegram |
| If: Output Type Selected | IF 判断 |
| Telegram: Send Transcript Message | Telegram |
| Set: Transcribed Audio Text | 数据设置 |
| Convert to TXT File | 转换为文件 |
| Send Transcript File | Telegram |

## 触发方式
- Telegram: Receive Message 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：multimodal-ai
