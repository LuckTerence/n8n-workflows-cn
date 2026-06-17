## 简介
**AI新闻简报构建**

Dumpling AI爬站+GPT-4o摘要+简报

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（GPT-4o→DeepSeek，Gmail需手动替换）
> 原始来源：https://n8nworkflows.xyz/workflows/4030

---

# AI新闻简报构建


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Get Website URLs from Google Sheet | Google Sheets |
| Crawl and Extract Site Content with Dumpling AI | HTTP Request |
| Split Extracted Results into Individual Items | 数据拆分 |
| Map Title, URL, and Page Text | 数据设置 |
|  Combine Articles into Single Prompt Format | Code |
|  Generate HTML Newsletter with Subject Using GPT-4o | OpenAI |
| Send Newsletter via Gmail | Gmail |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
