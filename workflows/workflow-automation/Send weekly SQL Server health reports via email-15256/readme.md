## 简介
**Send weekly SQL Server health reports via email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15256

---

# Send weekly SQL Server health reports via email


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| top slow queries | microsoftSql |
|  missing indexes | microsoftSql |
| index fragmentation | microsoftSql |
| blocking & wait stats | microsoftSql |
| Merge | 数据合并 |
| Code in JavaScript | Code |
| Send email | Email 发送 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
