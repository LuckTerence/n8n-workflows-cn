## 简介
**Automate Daily Outlook Calendar Digests to Microsoft Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6226

---

# Automate Daily Outlook Calendar Digests to Microsoft Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Calendar Events | Outlook |
| Create filter for "TODAY" value | Code |
| Schedule every midnight | 定时触发器 |
| Create chat message | Teams |
| HTML format | Code |



## 功能说明

日历日程管理，自动创建事件或发送提醒，定时执行。

定时触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：定时触发

## 触发方式
- Schedule every midnight 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
