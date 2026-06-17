## 简介
**Extract URLs from XML sitemaps to CSV via chat and HTTP request**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15443

---

# Extract URLs from XML sitemaps to CSV via chat and HTTP request


## 节点清单

| 节点 | 类型 |
|------|------|
| Listen for Sitemap URL | Chat 触发器 |
| Fetch Sitemap XML | HTTP Request |
| Check if URL is Accessible | IF 判断 |
| Alert User: Invalid URL | 聊天 |
| Parse XML to JSON Object | XML |
| Check for Sitemap Index | IF 判断 |
| Alert User: Index Not Supported | 聊天 |
| Extract URLs Array | 数据拆分 |
| Format URL Data | 数据设置 |
| Convert Data to CSV | 转换为文件 |
| Upload File to Host | HTTP Request |
| Format Final Output | Code |
| Send Download Link | 聊天 |
| Summarize Extraction Stats | 文本摘要 |
| Send Summary | 聊天 |
| Alert User: Upload Failed | 聊天 |

## 触发方式
- Listen for Sitemap URL 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：8
- 输出节点：7
- 分类：workflow-automation
