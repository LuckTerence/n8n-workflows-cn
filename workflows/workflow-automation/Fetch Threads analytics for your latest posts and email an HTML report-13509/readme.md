## 简介
**Fetch Threads analytics for your latest posts and email an HTML report**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13509

---

# Fetch Threads analytics for your latest posts and email an HTML report


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out | 数据拆分 |
| Fetch Threads Posts | HTTP Request |
| Fetch Post Insights | HTTP Request |
| Email Analytics Report | Email 发送 |
| Build HTML Report | Code |
| Merge Posts and Insights | Code |
| Get Threads Token | 数据表 |
| Set Token | 数据设置 |
| Manual Trigger | 手动触发 |
| Schedule Trigger (Every 2 Days) | 定时触发器 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：10
- 触发方式：手动触发, 定时触发

## 触发方式
- Manual Trigger 触发
- Schedule Trigger (Every 2 Days) 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
