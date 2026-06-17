## 简介
**Real-time PulsePoint Emergency Alerts to iMessage with AI Summaries**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5533

---

# Real-time PulsePoint Emergency Alerts to iMessage with AI Summaries


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Message | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| Merge all | Code |
| If | IF 判断 |
| OpenAI Chat Model | OpenAI Chat Model |
| Get alerts | Code |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：devops
