## 简介
**Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3701

---

# Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV


## 节点清单

| 节点 | 类型 |
|------|------|
| Convert to CSV File | 转换为文件 |
| Extract all books from the page | HTML |
| Sort by price | 数据排序 |
| Extract individual book price | HTML |
| Send CSV via e-mail | Email 发送 |
| Trigger- Watches For new URL in Spreadsheet | Google Sheets 触发器 |
| Scrape Website Content with Dumpling AI | HTTP Request |
| Split HTML Array into Individual Books | 数据拆分 |

## 触发方式
- Trigger- Watches For new URL in Spreadsheet 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
