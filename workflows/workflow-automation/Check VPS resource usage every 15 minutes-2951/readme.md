## 简介
**Check VPS resource usage every 15 minutes**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2951

---

# Check VPS resource usage every 15 minutes


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Email | Email 发送 |
| Check RAM usage | SSH |
| Check Disk usage | SSH |
| Check CPU usage | SSH |
| Merge check results | 数据合并 |
| Check results against thresholds | IF 判断 |
| Schedule Trigger | 定时触发器 |



## 功能说明

Check VPS resource usage every 15 minutes。

定时触发，通过 邮箱 实现自动化。

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

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
