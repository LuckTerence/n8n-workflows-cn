## 简介
**Automate Telegram Message Processing - Separate Text and Files**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9254

---

# Automate Telegram Message Processing - Separate Text and Files


## 节点清单

| 节点 | 类型 |
|------|------|
| Waiting For Message | Telegram 触发器 |
| Get Chat Message Only | 数据设置 |
| Switch | Switch 路由 |
| Split Out | 数据拆分 |
| Get Attachment Only | 数据设置 |
| Get & Download Attachment | Telegram |
| Get Attachment | 数据设置 |
| Next Step ! | 空操作 |
| Next Step ! | 空操作 |
| Next Step ! | 空操作 |
| Get Chat Message Content | 数据设置 |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：Telegram 消息触发

## 触发方式
- Waiting For Message 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
