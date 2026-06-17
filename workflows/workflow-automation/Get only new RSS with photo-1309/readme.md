## 简介
**Get only new RSS with photo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1309

---

# Get only new RSS with photo


## 节点清单

| 节点 | 类型 |
|------|------|
| Cron | 定时触发器 |
| RSS Feed Read | RSS Feed |
| Extract Image1 | htmlExtract |
| Filter RSS Data | 数据设置 |
| Only get new RSS1 | Function |

## 触发方式
- Cron 触发
- RSS Feed Read 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：3
- 输出节点：0
- 分类：workflow-automation
