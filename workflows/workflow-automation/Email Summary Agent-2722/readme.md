## 简介
**Email Summary Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2722

---

# Email Summary Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily 7AM Trigger | 定时触发器 |
| Fetch Emails - Past 24 Hours | Email 发送 |
| Organize Email Data - Morning | 数据聚合 |
| Summarize Emails with OpenAI - Morning | OpenAI |
| Send Summary - Morning | Email 发送 |

## 触发方式
- Daily 7AM Trigger 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
