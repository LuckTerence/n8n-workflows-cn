## 简介
**Create a Privacy-Focused AI Assistant with Telegram, Ollama, and Whisper**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6012

---

# Create a Privacy-Focused AI Assistant with Telegram, Ollama, and Whisper


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Get Voice File | Telegram |
| Message Type Switch | Switch 路由 |
| Authorization Check If | IF 判断 |
| Send a text message | Telegram |
| Whisper ASR HTTP Request | HTTP Request |
| Send a text message1 | Telegram |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |
| Rename Transcription Key | renameKeys |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
