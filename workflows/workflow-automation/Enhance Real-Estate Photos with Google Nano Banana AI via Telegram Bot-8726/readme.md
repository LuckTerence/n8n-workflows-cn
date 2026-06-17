## 简介
**Enhance Real-Estate Photos with Google Nano Banana AI via Telegram Bot**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8726

---

# Enhance Real-Estate Photos with Google Nano Banana AI via Telegram Bot


## 节点清单

| 节点 | 类型 |
|------|------|
| Nano Banana POST Request | HTTP Request |
| Wait 15 Secs | 等待 |
| GET Result from Nano Banana Node | HTTP Request |
| If | IF 判断 |
| Wait 15 Secs Again | 等待 |
| Telegram Trigger | Telegram 触发器 |
| Get a file | Telegram |
| Upload file | Google Drive |
| Send a photo message | Telegram |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
