## 简介
**Automate RSS News to Multi-Platform Social Media Publishing via PostPulse**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8800

---

# Automate RSS News to Multi-Platform Social Media Publishing via PostPulse


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| If | IF 判断 |
| Get connected accounts | postPulse |
| Media Check IF | IF 判断 |
| RSS Feed Read | RSS Feed |
| Merge (no media + accounts) | 数据合并 |
| Upload media | postPulse |
| Get upload status | postPulse |
| Merge1 | 数据合并 |
| If1 | IF 判断 |
| Wait | 等待 |
| Publish Post | postPulse |
| Merge | 数据合并 |
| Publish Post (text only) | postPulse |
| Limit to N Post | Function |

## 触发方式
- Schedule Trigger 触发
- RSS Feed Read 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
