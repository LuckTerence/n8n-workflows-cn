# Bypass Cloudflare Turnstile for Web Scraping with 2captcha

https://n8nworkflows.xyz/workflows/7151

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

## 触发方式
- Execute Workflow Trigger 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
