## 简介
**Scrape recent news about a company before a call**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2110

---

# Scrape recent news about a company before a call


## 节点清单

| 节点 | 类型 |
|------|------|
| Setup | 数据设置 |
| Extract company name | 数据设置 |
| Every morning @ 7 | 定时触发器 |
| Filter meetings | IF 判断 |
| Get latest news | HTTP Request |
| Format for email | Code |
| Send news | Email 发送 |
| No meetings today | 空操作 |
| Get meetings for today | Google Calendar |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

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

- 节点总数：9
- 触发方式：定时触发

## 触发方式
- Every morning @ 7 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
