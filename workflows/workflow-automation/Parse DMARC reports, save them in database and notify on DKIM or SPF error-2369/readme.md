## 简介
**Parse DMARC reports, save them in database and notify on DKIM or SPF error**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2369

---

# Parse DMARC reports, save them in database and notify on DKIM or SPF error


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| End date format | 日期时间 |
| If multiple records to parse | IF 判断 |
| Map fields for DB input and parse | 数据设置 |
| Begin format date | 日期时间 |
| Input into database | MySQL |
| If issue with DKIM or SPF | IF 判断 |
| Rename Keys | renameKeys |
| Rename column for consistency | 数据设置 |
| Unzip File | compression |
| Extract XML data | 从文件提取 |
| Parse XML data to JSON | XML |
| Split Out For Separate Entries | 数据拆分 |
| Slack Post Message On Channel | Slack |
| Send Error Notification Email | Email 发送 |



## 功能说明

数据库操作工具，自动查询或写入数据库。

手动触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：15
- 触发节点：0
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
