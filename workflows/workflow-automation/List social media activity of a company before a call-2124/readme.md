## 简介
**List social media activity of a company before a call**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2124

---

# List social media activity of a company before a call


## 节点清单

| 节点 | 类型 |
|------|------|
| Get recetn tweets | HTTP Request |
| Setup | 数据设置 |
| Every morning @ 7 | 定时触发器 |
| Get meetings for today | Google Calendar |
| Get attendees email domains | 数据设置 |
| Split Out | 数据拆分 |
| Get recent LinkedIn posts | HTTP Request |
| Enrich attendee company | clearbit |
| Gmail | Email 发送 |
| Format LinkedIn Posts | Code |
| Format Tweets | Code |
| Combine all activity for a company | 数据合并 |
| Extract data for email | 数据设置 |
| Prepare email template | HTML |
| Switch | Switch 路由 |
| Keep only ones with the domain | 过滤器 |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Every morning @ 7 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
