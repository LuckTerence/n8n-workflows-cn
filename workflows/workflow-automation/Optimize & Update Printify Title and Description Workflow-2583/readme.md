## 简介
**Optimize & Update Printify Title and Description Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：19 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2583

---

# Optimize & Update Printify Title and Description Workflow


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
