## 简介
**Automatically Send a Direct Message (DM) to New Followers on Bluesky using Baserow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2827

---

# Automatically Send a Direct Message (DM) to New Followers on Bluesky using Baserow


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Bluesky Session | HTTP Request |
| Run Daily at 9 AM | 定时触发器 |
| Set Bluesky Credentials | 数据设置 |
| Extract Followers Array | Code |
| Create Follower Record | baserow |
| Get Follower Record | baserow |
| If Follower Exists | IF 判断 |
| Limit | 数据限制 |
| Get All New Followers | baserow |
| Send Welcome Message | HTTP Request |
| Create Welcome Message | Code |
| Loop New Followers | 分批处理 |
| Loop Followers | 分批处理 |
| END OF WORKFLOW | 空操作 |
| Double Check If Welcome Has Already Been Sent | IF 判断 |
| Wait Follower Loop | 等待 |
| Wait New Follower Loop | 等待 |
| Get Firstname | Code |
| Update Follower Record to SentWelcome = TRUE | baserow |
| Get Latest Followers | HTTP Request |
| Get ConvoId | HTTP Request |



## 功能说明

Automatically Send a Direct Message (DM) to New Fo。

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

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- Run Daily at 9 AM 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：16
- 输出节点：4
- 分类：workflow-automation
