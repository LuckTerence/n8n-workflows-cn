## 简介
**Automate Docker Container Updates with Telegram Approval System**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3386

---

# Automate Docker Container Updates with Telegram Approval System


## 节点清单

| 节点 | 类型 |
|------|------|
| Pull n8n Image | SSH |
| docker compose pull | SSH |
| check n8n installed version | SSH |
| When clicking ‘Test workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| docker compose up | SSH |
| Set Default variable | 数据设置 |
| Github HTTP Request | HTTP Request |
| Merge Results | 数据合并 |
| Edit Version String | 数据设置 |
| Comapre Two Input | IF 判断 |
| Telegram Notif | Telegram |
| Telegram Approve | Telegram |
| Telegram Notif1 | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：8
- 输出节点：4
- 分类：devops
