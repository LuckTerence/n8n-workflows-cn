## 简介
**Monitor scheduled workflow health in n8n with automatic trigger checks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13290

---

# Monitor scheduled workflow health in n8n with automatic trigger checks


## 节点清单

| 节点 | 类型 |
|------|------|
| Test Run | 手动触发 |
| Daily Check at 9am | 定时触发器 |
| Fetch All Active Workflows | n8n |
| Discover Scheduled Workflows | Code |
| Get Latest Execution | n8n |
| Check for Stale Workflows | Code |
| Any Stale? | IF 判断 |
| Alert — Workflows Missed Schedule | 停止并报错 |
| All Healthy | 空操作 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：手动触发, 定时触发

## 触发方式
- Test Run 触发
- Daily Check at 9am 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
