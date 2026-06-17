## 简介
**Daily NASA Astronomy Picture Delivered to Your Inbox via Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7290

---

# Daily NASA Astronomy Picture Delivered to Your Inbox via Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Send email | Email 发送 |
| Summarize | 文本摘要 |
| Set only important fields | 数据设置 |
| Filter only last 2 days | 过滤器 |
| Schedule Trigger | 定时触发器 |
| Get APOD Data | RSS Feed |
| Aggregate data | 数据设置 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- Get APOD Data 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
