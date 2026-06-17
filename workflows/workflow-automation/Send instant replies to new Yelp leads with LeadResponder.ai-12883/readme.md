## 简介
**Send instant replies to new Yelp leads with LeadResponder.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：3 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/12883

---

# Send instant replies to new Yelp leads with LeadResponder.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Call to check new leads | HTTP Request |
| Prepare message for reply | Code |
| Push message as a reply to a new lead. | HTTP Request |
| Schedule Trigger for 1 minute check | 定时触发器 |

## 触发方式
- Schedule Trigger for 1 minute check 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：1
- 输出节点：2
- 分类：workflow-automation
