## 简介
**Extract Public Email Addresses From Any Website Using Firecrawl**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5786

---

# Extract Public Email Addresses From Any Website Using Firecrawl


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| map_website | HTTP Request |
| start_batch_scrape | HTTP Request |
| check_retry_count | IF 判断 |
| too_many_attempts_error | 停止并报错 |
| rate_limit_wait | 等待 |
| set_result | 数据设置 |
| check_scrape_completed | IF 判断 |
| fetch_scrape_results | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
