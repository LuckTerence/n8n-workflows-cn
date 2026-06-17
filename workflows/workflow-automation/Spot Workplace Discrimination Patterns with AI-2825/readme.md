## 简介
**Spot Workplace Discrimination Patterns with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2825

---

# Spot Workplace Discrimination Patterns with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Merge | 数据合并 |
| OpenAI Chat Model | OpenAI Chat Model |
| SET company_name | 数据设置 |
| Define dictionary of demographic keys | 数据设置 |
| ScrapingBee Search Glassdoor | HTTP Request |
| Extract company url path | HTML |
| ScrapingBee GET company page contents | HTTP Request |
| Extract reviews page url path | HTML |
| ScrapingBee GET Glassdoor Reviews Content | HTTP Request |
| Extract Overall Review Summary | HTML |
| Extract Demographics Module | HTML |
| Extract overall ratings and distribution percentages | 信息提取器 |
| Extract demographic distributions | 信息提取器 |
| Define contributions to variance | 数据设置 |
| Set variance and std_dev | 数据设置 |
| Calculate P-Scores | Code |
| Sort Effect Sizes | 数据设置 |
| Calculate Z-Scores and Effect Sizes | 数据设置 |
| Format dataset for scatterplot | Code |
| Specify additional parameters for scatterplot | 数据设置 |
| Quickchart Scatterplot | HTTP Request |
| QuickChart Bar Chart | quickChart |
| Text Analysis of Bias Data | LLM Chain |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：21
- 输出节点：4
- 分类：workflow-automation
