## 简介
**Create a Simple Data Caching System with No External Dependencies**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9369

---

# Create a Simple Data Caching System with No External Dependencies


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Upsert row(s) | 数据表 |
| Return Value | 数据设置 |
| Action Write Value | 空操作 |
| Get row(s) | 数据表 |
| If Expired Cache | IF 判断 |
| Read Action | 空操作 |
| Check Action Type | IF 判断 |
| If not in Cache | IF 判断 |
| No cache found, use error detection to detect this. | 停止并报错 |
| Return Value from Cache | 数据设置 |
| 1 Hour Clean for Cache Table | 定时触发器 |
| Drop all rows with expired cache entires | 数据表 |

## 触发方式
- When Executed by Another Workflow 触发
- 1 Hour Clean for Cache Table 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
