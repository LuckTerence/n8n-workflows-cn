## 简介
**Automated Property Lead Generation with BatchData and CRM Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3665

---

# Automated Property Lead Generation with BatchData and CRM Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Market Scan | 定时触发器 |
| BatchData API Configuration | 数据设置 |
| Query BatchData Properties | HTTP Request |
| Get Previous Results | Code |
| Compare Results | Code |
| Split Properties | 数据拆分 |
| Filter High Potential | 过滤器 |
| Get Property Details | HTTP Request |
| Format Email Content | 数据设置 |
| Send Email Alert | Email 发送 |
| Post to Slack | Slack |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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
- 触发方式：定时触发

## 触发方式
- Schedule Market Scan 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
