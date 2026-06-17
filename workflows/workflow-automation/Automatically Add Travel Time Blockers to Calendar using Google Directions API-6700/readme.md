## 简介
**Automatically Add Travel Time Blockers to Calendar using Google Directions API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6700

---

# Automatically Add Travel Time Blockers to Calendar using Google Directions API


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| get_calendar_events | Google Calendar 工具 |
| create_calendar_event | Google Calendar 工具 |
| travel_directions | 工作流工具 |
| set Travel_time | 数据设置 |
| Call Google Directions API | HTTP Request |
| Sub: travel_directions | 执行工作流触发器 |
| Set Defaults | 数据设置 |



## 功能说明

日历日程管理，自动创建事件或发送提醒，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

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
- Sub: travel_directions 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
