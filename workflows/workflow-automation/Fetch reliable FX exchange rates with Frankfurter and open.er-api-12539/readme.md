## 简介
**Fetch reliable FX exchange rates with Frankfurter and open.er-api**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12539

---

# Fetch reliable FX exchange rates with Frankfurter and open.er-api


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Currencies | 数据设置 |
| If Valid Data | IF 判断 |
| Stop and Error | 停止并报错 |
| Frankfurter | HTTP Request |
| Normalize Frankfurter | Code |
| open.er-api.com | HTTP Request |
| If base correct 1 | IF 判断 |
| If base correct  2 | IF 判断 |
| Fetch FX Rates | 执行工作流触发器 |
| Stop and Error3 | 停止并报错 |
| Normalize open.er-api.com | Code |
| Handle Wrong Base 1 | Code |
| Handle Wrong Base 2 | Code |
| Trim | Code |
| If Trim | IF 判断 |
| Manual Trigger (Example) | 手动触发 |
| Validate & Normalize Inputs | Code |
| Initialize FX State + Static Rates | Code |
| Initialize Coverage Tracking | Code |
| Merge Rates & Check Coverage (1) | Code |
| Merge Rates & Check Coverage (2) | Code |
| Coverage Complete 1? | IF 判断 |
| Coverage Complete 2? | IF 判断 |
| Final Output | 空操作 |

## 触发方式
- Fetch FX Rates 触发
- Manual Trigger (Example) 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：20
- 输出节点：2
- 分类：workflow-automation
