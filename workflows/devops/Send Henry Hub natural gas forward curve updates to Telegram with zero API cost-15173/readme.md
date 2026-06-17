## 简介
**Send Henry Hub natural gas forward curve updates to Telegram with zero API cost**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15173

---

# Send Henry Hub natural gas forward curve updates to Telegram with zero API cost


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Natural Gas Page1 | HTTP Request |
| Market Hours Trigger1 | 定时触发器 |
| Extract Spot & Futures1 | Code |
| Build HTML Table1 | Code |
| Send Telegram Update1 | Telegram |



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

- 节点总数：5
- 触发方式：定时触发

## 触发方式
- Market Hours Trigger1 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：devops
