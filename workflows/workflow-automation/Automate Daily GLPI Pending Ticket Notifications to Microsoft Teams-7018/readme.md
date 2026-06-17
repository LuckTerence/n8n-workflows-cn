## 简介
**Automate Daily GLPI Pending Ticket Notifications to Microsoft Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7018

---

# Automate Daily GLPI Pending Ticket Notifications to Microsoft Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Get pending cases | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| No Operation, do nothing | 空操作 |
| Create chat message | Teams |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| No Operation, do nothing1 | 空操作 |
| Get session token | HTTP Request |
| Are there any ongoing cases? | IF 判断 |
| End session | HTTP Request |



## 功能说明

通知推送系统，多渠道消息分发，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
