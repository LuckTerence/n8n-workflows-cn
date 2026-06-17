## 简介
**Create a Weekly Responsive Plex Media Newsletter via Email (Tautulli Alternative)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7556

---

# Create a Weekly Responsive Plex Media Newsletter via Email (Tautulli Alternative)


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Fetch Recent Movies | HTTP Request |
| Fetch Recent TV Shows | HTTP Request |
| Combine Movie & TV Data | 数据合并 |
| Generate HTML Newsletter | Code |
| Prepare Emails for Recipients | Code |
| Send Newsletter Emails | Email 发送 |
| Finish | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
