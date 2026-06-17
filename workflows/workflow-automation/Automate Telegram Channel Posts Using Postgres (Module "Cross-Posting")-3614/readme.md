## 简介
**Automate Telegram Channel Posts Using Postgres (Module "Cross-Posting")**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3614

---

# Automate Telegram Channel Posts Using Postgres (Module "Cross-Posting")


## 节点清单

| 节点 | 类型 |
|------|------|
| Variables TG | 数据设置 |
| Initialization | 数据设置 |
| Telegram Trigger | Telegram 触发器 |
| Select Channels | PostgreSQL |
| Is Admin? | IF 判断 |
| Add Channel | PostgreSQL |
| Get Bot Status | PostgreSQL |
| Define flow | Switch 路由 |
| Commands | Switch 路由 |
| Channel Exists | Telegram |
| Request Add Channel | Telegram |
| Request Delete Channel | Telegram |
| Request New Delete Channel | Telegram |
| Request New Add Channel | Telegram |
| Channel Not Exists | Telegram |
| Delete Channel | PostgreSQL |
| Get Channels | PostgreSQL |
| Add Divide Channels | 文本摘要 |
| Channels | Telegram |
| Define Type | Switch 路由 |
| Get Channels | PostgreSQL |
| If | IF 判断 |
| Upsert bot status on START | PostgreSQL |
| Buttons | Switch 路由 |
| Update bot status on ADD CHANNEL | PostgreSQL |
| Update bot status on DELETE CHANNEL | PostgreSQL |
| Success Send Post | Telegram |
| Update bot status on START | PostgreSQL |
| Welcome Message | Telegram |
| Update bot status on POST TEXT REQUEST | PostgreSQL |
| Request Post Text | Telegram |
| Request Post Image Text | Telegram |
| Update bot status on POST IMAGE REQUEST TEXT | PostgreSQL |
| Update bot status on POST IMAGE REQUEST IMAGE | PostgreSQL |
| Select Channels | PostgreSQL |
| Request Post Image Image | Telegram |
| Success Send Post Image | Telegram |
| Update bot status on START | PostgreSQL |
| If1 | IF 判断 |
| Send Posts (4922) | Telegram |
| Send Posts Image (4922) | Telegram |
| Send Posts Image (4922) | Telegram |
| Upsert bot status on START | PostgreSQL |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：43
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：26
- 输出节点：16
- 分类：workflow-automation
