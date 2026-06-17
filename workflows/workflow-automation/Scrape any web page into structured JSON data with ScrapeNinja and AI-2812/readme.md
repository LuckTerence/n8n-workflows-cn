## 简介
**Scrape any web page into structured JSON data with ScrapeNinja and AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2812

---

# Scrape any web page into structured JSON data with ScrapeNinja and AI


## 节点清单

| 节点 | 类型 |
|------|------|
| ScrapeNinja | scrapeNinja |
| Google Gemini Chat Model | OpenAI Chat Model |
| Generate custom web scraper | 手动触发 |
| Cleanup HTML | scrapeNinja |
| Generate JS eval code via LLM | LLM Chain |
| Eval generated code to extract data | scrapeNinja |

## 触发方式
- Generate custom web scraper 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：5
- 输出节点：0
- 分类：workflow-automation
