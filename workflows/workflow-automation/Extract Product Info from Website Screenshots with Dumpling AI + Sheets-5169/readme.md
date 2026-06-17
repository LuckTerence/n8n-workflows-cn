## 简介
**Extract Product Info from Website Screenshots with Dumpling AI + Sheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5169

---

# Extract Product Info from Website Screenshots with Dumpling AI + Sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Watch for New Screenshot URLs in Google Sheets | Google Sheets 触发器 |
| Create Screenshot File via Dumpling AI | HTTP Request |
| Download Screenshot Image File from Dumpling AI | HTTP Request |
| Extract Text from Screenshot with Dumpling AI | HTTP Request |
| Convert Image File to Base64 | 从文件提取 |
| Format Extracted Data for Google Sheets | 数据设置 |
| Save extracted data to Google Sheets | Google Sheets |

## 触发方式
- Watch for New Screenshot URLs in Google Sheets 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
