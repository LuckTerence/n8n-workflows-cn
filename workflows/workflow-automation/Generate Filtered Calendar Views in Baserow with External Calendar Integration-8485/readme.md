## 简介
**Generate Filtered Calendar Views in Baserow with External Calendar Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8485

---

# Generate Filtered Calendar Views in Baserow with External Calendar Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Create a token | HTTP Request |
| Share the view | HTTP Request |
| Update the url's | baserow |
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Baserow credentials | 数据设置 |
| Set table and field ids | 数据设置 |
| Get all records from filter table | baserow |
| Create new calendar view | HTTP Request |
| Create filter | HTTP Request |
| Set background color | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：workflow-automation
