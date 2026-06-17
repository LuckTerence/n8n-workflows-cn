## 简介
**Monitor Security Advisories**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1974

---

# Monitor Security Advisories


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Get Palo Alto security advisories | RSS Feed |
| GlobalProtect advisory? | 过滤器 |
| Traps advisory? | 过滤器 |
| Create Jira issue | jira |
| Get customers | n8nTrainingCustomerDatastore |
| Email customers | Email 发送 |
| Extract info | 数据设置 |
| Check if posted in last 24 hours | IF 判断 |
| Ignore, stale advisory | 空操作 |
| Run workflow every 24 hours at 1am | 定时触发器 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 邮箱 实现自动化。

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

- 节点总数：11
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking "Execute Workflow" 触发
- Get Palo Alto security advisories 触发
- Run workflow every 24 hours at 1am 触发

## 统计
- 节点总数：11
- 触发节点：3
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
