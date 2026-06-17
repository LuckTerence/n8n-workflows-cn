## 简介
**Send links from Telegram Channel to Hoarder and Readeck**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
