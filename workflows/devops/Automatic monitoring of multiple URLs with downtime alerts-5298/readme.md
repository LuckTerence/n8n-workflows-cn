## 简介
**Automatic monitoring of multiple URLs with downtime alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5298

---

# Automatic monitoring of multiple URLs with downtime alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| URLs | 数据设置 |
| Success | Google Sheets |
| Error | Google Sheets |
| Total | 文本摘要 |
| Bucle URLs | 分批处理 |
| Run trigger | 手动触发 |
| Send a message | Email 发送 |
| Code | Code |
| Split Out2 | 数据拆分 |
| Request | HTTP Request |

## 触发方式
- Schedule Trigger 触发
- Run trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：8
- 输出节点：2
- 分类：devops
