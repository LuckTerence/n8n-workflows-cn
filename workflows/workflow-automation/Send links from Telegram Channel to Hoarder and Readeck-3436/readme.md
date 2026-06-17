## 简介
**Send links from Telegram Channel to Hoarder and Readeck**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3436

---

# Send links from Telegram Channel to Hoarder and Readeck


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| not_saved_links_hd | Code |
| not_saved_links_rd | Code |
| saved_links_rd | 数据设置 |
| save_link_rd | HTTP Request |
| save_link_hd | HTTP Request |
| get_links_rd | HTTP Request |
| get_links_hd | HTTP Request |
| saved_links_hd | 数据设置 |
| channel_links_tg | Code |
| channel_items_tg | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
