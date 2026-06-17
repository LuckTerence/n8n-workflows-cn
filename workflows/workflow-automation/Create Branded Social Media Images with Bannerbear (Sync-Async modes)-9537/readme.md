## 简介
**Create Branded Social Media Images with Bannerbear (Sync-Async modes)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9537

---

# Create Branded Social Media Images with Bannerbear (Sync-Async modes)


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| SetParameters | 数据设置 |
| SynchronouslyCreateImage | HTTP Request |
| GetImageUrlAndSize | 数据设置 |
| Webhook_OnImageCreated | Webhook |
| GetUidAndStatus | 数据设置 |
| GetCompletedImageInfo | 数据设置 |
| IfSynchrounousCall | IF 判断 |
| AsynchronouslyCreateImage | bannerbear |



## 功能说明

AI 图像生成工作流，文生图或图生图，Webhook 触发。

Webhook触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：手动触发, Webhook 触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Webhook_OnImageCreated 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
