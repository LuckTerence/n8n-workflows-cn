## 简介
**Generate daily tech, manga & movies newsletter from RSS feeds with Brevo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11806

---

# Generate daily tech, manga & movies newsletter from RSS feeds with Brevo


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out2 | 数据拆分 |
| Schedule Trigger | 定时触发器 |
| RSS Read1 | RSS Feed |
| Loop Over Items3 | 分批处理 |
| Rss database | Google Sheets |
| Switch | Switch 路由 |
| Code in Python (Beta) | Code |
| RSS Read2 | RSS Feed |
| Loop Over Items4 | 分批处理 |
| Code in Python (Beta)1 | Code |
| RSS Read3 | RSS Feed |
| Loop Over Items5 | 分批处理 |
| Code in Python (Beta)2 | Code |
| Aggregate | 数据聚合 |
| Merge | 数据合并 |
| Send a Mail | Email 发送 |
| Mail Campaign | sendInBlue |
| HTML Template | HTML |
| Category Rss | 数据设置 |
| Jeu video | Code |
| Movie | Code |
| Manga | Code |



## 功能说明

内容管理工具，自动生成或发布内容，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- RSS Read1 触发
- RSS Read2 触发
- RSS Read3 触发

## 统计
- 节点总数：22
- 触发节点：4
- 处理节点：17
- 输出节点：1
- 分类：workflow-automation
