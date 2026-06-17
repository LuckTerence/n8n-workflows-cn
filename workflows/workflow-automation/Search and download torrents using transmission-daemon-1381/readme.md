## 简介
**Search and download torrents using transmission-daemon**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1381

---

# Search and download torrents using transmission-daemon


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| SearchTorrent | functionItem |
| Start download | HTTP Request |
| IF | IF 判断 |
| Torrent not found | Telegram |
| Telegram1 | Telegram |
| IF2 | IF 判断 |
| Start download new token | HTTP Request |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
