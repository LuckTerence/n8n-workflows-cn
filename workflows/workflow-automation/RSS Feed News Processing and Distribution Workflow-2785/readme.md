## 简介
**RSS Feed News Processing and Distribution Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2785

---

# RSS Feed News Processing and Distribution Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| RSS Read Testing Catalog | RSS Feed |
| Transform date | 数据设置 |
| Filter by date (more than 7 days) | 过滤器 |
| Sort by date | 数据排序 |
| Limit news to x | 数据限制 |
| Transform new to MD | Code |
| Publish comment | trello |
| Send revision email | Email 发送 |
| Merge | 数据合并 |
| RSS Read marktechpost | RSS Feed |
| RSS Read | RSS Feed |



## 功能说明

内容管理工具，自动生成或发布内容，定时执行。

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

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- RSS Read Testing Catalog 触发
- RSS Read marktechpost 触发
- RSS Read 触发

## 统计
- 节点总数：12
- 触发节点：4
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
