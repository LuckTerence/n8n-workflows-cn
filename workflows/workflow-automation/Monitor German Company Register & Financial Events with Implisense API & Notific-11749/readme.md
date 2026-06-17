## 简介
**Monitor German Company Register & Financial Events with Implisense API & Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11749

---

# Monitor German Company Register & Financial Events with Implisense API & Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Batches | 分批处理 |
| Rate Limit | 等待 |
| API Success? | IF 判断 |
| Normalize Events | Code |
| Log API Error | Code |
| Merge Results | 数据合并 |
| Filter Relevant | IF 判断 |
| Deduplicate | 去重 |
| Prepare Notification | Code |
| Notification Sent? | IF 判断 |
| Log Success | Code |
| Log Failed | Code |
| Merge Notifications | 数据合并 |
| Loop Continue | 空操作 |
| Create Summary | Code |
| Lookup Company | HTTP Request |
| Get Events | HTTP Request |
| Config | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Mock Lead Input | Function |
| Email, Chat, Webhook etc. | 空操作 |



## 功能说明

监控告警系统，异常检测并发送通知。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：21
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：18
- 输出节点：2
- 分类：workflow-automation
