## 简介
**Proxmox System Monitor - VM Status, Host Resources & Temperature Alerts via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9733

---

# Proxmox System Monitor - VM Status, Host Resources & Temperature Alerts via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Every 15min | 定时触发器 |
| Set Variables | 数据设置 |
| Proxmox Login | HTTP Request |
| Prepare Auth | 数据设置 |
| API - VM List | HTTP Request |
| API - Node Tasks | HTTP Request |
| API - Node Status | HTTP Request |
| SSH - Get Sensors | SSH |
| Process Data | Code |
| Generate Formatted Message | Code |
| Send Telegram Report | Telegram |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

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

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Schedule Every 15min 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：5
- 输出节点：5
- 分类：workflow-automation
