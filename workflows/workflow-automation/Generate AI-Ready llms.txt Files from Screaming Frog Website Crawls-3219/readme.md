## 简介
**Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3219

---

# Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls


## 节点清单

| 节点 | 类型 |
|------|------|
| Set useful fields | 数据设置 |
| Text Classifier | 文本分类器 |
| OpenAI Chat Model | OpenAI Chat Model |
| No Operation, do nothing | 空操作 |
| Filter URLs | 过滤器 |
| Summarize - Concatenate | 文本摘要 |
| Set Fields - llms.txt Content | 数据设置 |
| upload file anywhere | 空操作 |
| Set Field - llms.txt Row | 数据设置 |
| Form - Screaming frog internal_html.csv upload | 表单触发器 |
| Extract data from Screaming Frog file | 从文件提取 |
| Generate llms.txt file | 转换为文件 |

## 触发方式
- Form - Screaming frog internal_html.csv upload 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
