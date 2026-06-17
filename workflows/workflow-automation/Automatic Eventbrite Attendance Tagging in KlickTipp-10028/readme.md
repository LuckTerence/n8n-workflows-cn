## 简介
**Automatic Eventbrite Attendance Tagging in KlickTipp**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10028

---

# Automatic Eventbrite Attendance Tagging in KlickTipp


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger every 15min | 定时触发器 |
| Tag contact for non attendance | Klicktipp |
| Attendance check | Switch 路由 |
| Split attendee list | 数据拆分 |
| List Evenbrite attendees from event | HTTP Request |
| Tag contact for attendance | Klicktipp |



## 功能说明

Automatic Eventbrite Attendance Tagging in KlickTi。

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

- 节点总数：6
- 触发方式：定时触发

## 触发方式
- Trigger every 15min 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
