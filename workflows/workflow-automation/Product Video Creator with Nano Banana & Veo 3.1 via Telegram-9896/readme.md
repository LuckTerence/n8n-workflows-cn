## 简介
**Product Video Creator with Nano Banana & Veo 3.1 via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9896

---

# Product Video Creator with Nano Banana & Veo 3.1 via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Image to Base64 | 从文件提取 |
| AI Design Analysis | OpenAI Chat Model |
| Combine Image & Analysis | 数据合并 |
| Prepare API Payload | Code |
| Generate Enhanced Image | HTTP Request |
| Convert Base64 to Image (only image) | 转换为文件 |
| Convert Base64 to Image (image and text) | 转换为文件 |
| Initiate veo 3.1 Video Generation | HTTP Request |
| Check Video Status | HTTP Request |
| Video Ready Validator | IF 判断 |
| Processing Delay (30s) | 等待 |
| Convert Base64 to video | 转换为文件 |
| Download Image File | Telegram |
| Telegram Trigger Received | Telegram 触发器 |
| Send veo 3.1 video | Telegram |

## 触发方式
- Telegram Trigger Received 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：9
- 输出节点：5
- 分类：workflow-automation
