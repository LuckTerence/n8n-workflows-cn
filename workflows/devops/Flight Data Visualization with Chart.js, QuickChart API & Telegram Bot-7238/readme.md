## 简介
**Flight Data Visualization with Chart.js, QuickChart API & Telegram Bot**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7238

---

# Flight Data Visualization with Chart.js, QuickChart API & Telegram Bot


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Check Start | IF 判断 |
| Send Welcome Message | Telegram |
| Switch | Switch 路由 |
| Extract from File | 从文件提取 |
| Read CSV File | 读写文件 |
| Process Data & Create Bar Chart | Code |
| Fetch Bar Chart Image | HTTP Request |
| Send Bar Chart to Telegram | Telegram |
| Process Data & Create Pie Chart | Code |
| Fetch Pie Chart Image | HTTP Request |
| Send Pie Chart to Telegram | Telegram |
| Fetch Doughnut Chart Image | HTTP Request |
| Send Doughnut Chart to Telegram | Telegram |
| Process Data & Create Line Chart | Code |
| Process Data & Create Doughnut Chart | Code |
| Fetch Line Chart Image | HTTP Request |
| Send Line Chart to Telegram | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：18
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：8
- 输出节点：9
- 分类：devops
