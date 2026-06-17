# Optimize & Update Printify Title and Description Workflow

https://n8nworkflows.xyz/workflows/2583

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Printify - Get Shops | HTTP Request |
| Printify - Get Products | HTTP Request |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Split - id, title, desc | 数据拆分 |
| Calculator | 计算器工具 |
| Wikipedia | Wikipedia 工具 |
| Printify - Update Product | HTTP Request |
| Brand Guidelines + Custom Instructions | 数据设置 |
| Google Sheets Trigger | Google Sheets 触发器 |
| Printify - Get Shops1 | HTTP Request |
| GS - Add Product Option | Google Sheets |
| Update Product Option | Google Sheets |
| If1 | IF 判断 |
| Number of Options | 数据设置 |
| Calculate Options | Code |
| Remember Options | 数据设置 |
| Generate Title and Desc | OpenAI |
| If | IF 判断 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Google Sheets Trigger 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：14
- 输出节点：4
- 分类：workflow-automation
