## 简介
**Bypass Cloudflare Turnstile for Web Scraping with 2captcha**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7151

---

# Bypass Cloudflare Turnstile for Web Scraping with 2captcha


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute Workflow Trigger | 执行工作流触发器 |
| Set destination_url value | 数据设置 |
| Get destination web page | HTTP Request |
| Extract Turnstile Sitekey | Code |
| Wait 30 seconds | 等待 |
| Create Captcha Task | HTTP Request |
| Get Captcha Solution | HTTP Request |
| No operation - return loop | 空操作 |
| Raise runIndex error | 停止并报错 |
| When clicking ‘Test workflow’ | 手动触发 |
| Check Captcha Status | Switch 路由 |
| Puppeteer | puppeteer |
| Pass CF Turnstile check using 2Captcha | 执行工作流 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- Execute Workflow Trigger 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
