## 简介
**Nano Banana AI Image Editor via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8082

---

# Nano Banana AI Image Editor via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Photo Message Receiver | Telegram 触发器 |
| Download Telegram Photo | Telegram |
| Convert Photo to Base64 | 从文件提取 |
| Format Image Data URL | Code |
| Parse AI Response Data | 数据设置 |
| Base64 to Binary File | 转换为文件 |
| Send Processed Photo | Telegram |
| Nano Banana Image Processor | HTTP Request |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

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

- 节点总数：8
- 触发方式：Telegram 消息触发

## 触发方式
- Photo Message Receiver 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
