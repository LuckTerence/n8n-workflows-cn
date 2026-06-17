## 简介
**Generate Local Business Leads with Google Places API & Website Email Scraping**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11360

---

# Generate Local Business Leads with Google Places API & Website Email Scraping


## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger | 表单触发器 |
| Parse Form Data | 数据设置 |
| Create Search Combinations | 数据设置 |
| Split Into Searches | 数据拆分 |
| Extract Place Info | Code |
| Wait (Rate Limit) | 等待 |
| Get Business Details | HTTP Request |
| Merge Details | 数据设置 |
| Has Website? | IF 判断 |
| Extract Emails & Clean | Code |
| No Website Fallback | 数据设置 |
| Convert to CSV | 转换为文件 |
| Google Places Search1 | HTTP Request |
| Scrape Website1 | HTTP Request |
| Merge | 数据合并 |
| Final Data | 数据设置 |
| Loop Over Items | 分批处理 |
| Loop Over Items1 | 分批处理 |
| Wait | 等待 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：19
- 触发方式：表单提交触发

## 触发方式
- Form Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：15
- 输出节点：3
- 分类：workflow-automation
