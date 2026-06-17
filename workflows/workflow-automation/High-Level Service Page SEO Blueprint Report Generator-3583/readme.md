## 简介
**High-Level Service Page SEO Blueprint Report Generator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3583

---

# High-Level Service Page SEO Blueprint Report Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| Convert URLs to Items | Code |
| Start | 表单触发器 |
| Loop Over Items | 分批处理 |
| Get URL HTML | HTTP Request |
| Extract HTML Elements | Code |
| Set URL Data | 数据设置 |
| Code | Code |
| Edit Fields1 | 数据设置 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Wait | 等待 |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Set Competitor Analysis | 数据设置 |
| Set User Intent Analysis | 数据设置 |
| Wait1 | 等待 |
| Google Gemini Chat Model2 | OpenAI Chat Model |
| Competitors Analysis | LLM Chain |
| User Intent Analysis | LLM Chain |
| Synthesis & Gap Analysis | LLM Chain |
| Set Synthesis & Gap Analysis | 数据设置 |
| Wait2 | 等待 |
| Google Gemini Chat Model3 | OpenAI Chat Model |
| Ideal Page Outline Generation | LLM Chain |
| Set Page Outline | 数据设置 |
| Wait3 | 等待 |
| Google Gemini Chat Model4 | OpenAI Chat Model |
| UX, Conversion & Copywriting Enhancement | LLM Chain |
| Set UX & Conversions Enhancements | 数据设置 |
| Google Gemini Chat Model5 | OpenAI Chat Model |
| Final Service Page Blueprint | LLM Chain |
| Edit Fields2 | 数据设置 |
| Convert to File | 转换为文件 |
| Edit Fields | 数据设置 |

## 触发方式
- Start 触发

## 统计
- 节点总数：32
- 触发节点：1
- 处理节点：30
- 输出节点：1
- 分类：workflow-automation
