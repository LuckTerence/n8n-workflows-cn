## 简介
**Automatic monitoring of multiple URLs with downtime alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5298

---

# Automatic monitoring of multiple URLs with downtime alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Split Out | 数据拆分 |
| URLs | 数据设置 |
| Success | Google Sheets |
| Error | Google Sheets |
| Total | 文本摘要 |
| Bucle URLs | 分批处理 |
| Run trigger | 手动触发 |
| Send a message | Email 发送 |
| Code | Code |
| Split Out2 | 数据拆分 |
| Request | HTTP Request |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

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
- 触发方式：定时触发, 手动触发

## 触发方式
- Schedule Trigger 触发
- Run trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：8
- 输出节点：2
- 分类：devops
