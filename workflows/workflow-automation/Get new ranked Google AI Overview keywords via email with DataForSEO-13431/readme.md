## 简介
**Get new ranked Google AI Overview keywords via email with DataForSEO**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13431

---

# Get new ranked Google AI Overview keywords via email with DataForSEO


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| Get ranked keywords | dataForSeoLabsApi |
| Get previous keywords | Google Sheets |
| Get targets | Google Sheets |
| Append keyword in sheet | Google Sheets |
| Run every Monday | 定时触发器 |
| Aggregate1 | 数据聚合 |
| Clear sheet | Google Sheets |
| Send a message | Email 发送 |
| Initialize "items" field | 数据设置 |
| Set "items" field | 数据设置 |
| Merge "items" with DFS response | 数据设置 |
| Has more pages? | IF 判断 |
| Merge "items" with last response | 数据设置 |
| Filter (has new AIO keywords) | 过滤器 |
| Find new AIO keywords | Code |
| Split out (items) | 数据拆分 |
| Loop over targets | 分批处理 |



## 功能说明

邮件自动化处理，AI 分类整理或。

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

- 节点总数：18
- 触发方式：定时触发

## 触发方式
- Run every Monday 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：16
- 输出节点：1
- 分类：workflow-automation
