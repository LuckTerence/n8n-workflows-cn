## 简介
**Extract Company Data and Calculate ICP Score with Airtop**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4260

---

# Extract Company Data and Calculate ICP Score with Airtop


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Merge | 数据合并 |
| Extract company LinkedIn url | 执行工作流 |
| Extract Company Information | 执行工作流 |
| Calclate ICP | 执行工作流 |
| LinkedIn link exists? | IF 判断 |
| Is valid LinkedIn link? | 过滤器 |
| Unify Params | 数据设置 |

## 触发方式
- On form submission 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
