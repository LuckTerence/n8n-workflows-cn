## 简介
**Generate Newsletter Images with Nano Banana & Post Human-Approved Tweets to X**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：19 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/8655

---

# Generate Newsletter Images with Nano Banana & Post Human-Approved Tweets to X


## 节点清单

| 节点 | 类型 |
|------|------|
| Image Gen (Nano Banana) | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| Wait1 | 等待 |
| Get Image | HTTP Request |
| Image created | IF 判断 |
| Google Sheets Trigger | Google Sheets 触发器 |
| post media | HTTP Request |
| Add Image URL | Google Sheets |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Send Tweet text for approval | Telegram |
| Send Tweet image for approval | Telegram |
| Approved | IF 判断 |
| Tweet not approved | Google Sheets |
| Download Image | HTTP Request |
| Downlaod Image again | HTTP Request |
| Create Tweet | Twitter |
| Tweet Generator | AI Agent |
| Prompt Generator | AI Agent |
| Tweet posted | Google Sheets |

## 触发方式
- Google Sheets Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
