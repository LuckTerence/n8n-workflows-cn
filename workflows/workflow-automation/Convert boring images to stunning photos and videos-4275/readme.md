## 简介
**Convert boring images to stunning photos and videos**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4275

---

# Convert boring images to stunning photos and videos


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Bot Trigger | Telegram 触发器 |
| Edit Image (OpenAI) | HTTP Request |
| Convert to Binary Image | 转换为文件 |
| Send Edited Image | Telegram |
| Generate Variation (Replicate) | HTTP Request |
| Retrieve Generated Image | HTTP Request |
| Send Variation Image | Telegram |
| Get File Path | HTTP Request |
| Wait for Processing | 等待 |



## 功能说明

AI 图像生成工作流，文生图或图生图。

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

- 节点总数：9
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Bot Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：2
- 输出节点：6
- 分类：workflow-automation
