## 简介
**Auto Update n8n to Latest Version with Coolify**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4360

---

# Auto Update n8n to Latest Version with Coolify


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Release | HTTP Request |
| Update ENV | HTTP Request |
| Deploy | HTTP Request |
| Filter | 过滤器 |
| Limit | 数据限制 |
| Remove Duplicates | 去重 |
| Get Releases | HTTP Request |
| Auto Update Latest Release | 定时触发器 |
| Auto Update Beta Release | 定时触发器 |

## 触发方式
- Auto Update Latest Release 触发
- Auto Update Beta Release 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
