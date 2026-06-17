## 简介
**Merge and filter several Rss & send to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2748

---

# Merge and filter several Rss & send to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Olimpo | RSS Feed |
| Edit Fields | 数据设置 |
| Edit Fields1 | 数据设置 |
| Merged Rss | 数据合并 |
| Sort | 数据排序 |
| Markdown list | Code |
| Telegram | Telegram |
| Schedule Trigger | 定时触发器 |
| Filter | 过滤器 |
| RSS Torrent | RSS Feed |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- RSS Olimpo 触发
- Schedule Trigger 触发
- RSS Torrent 触发

## 统计
- 节点总数：10
- 触发节点：3
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
