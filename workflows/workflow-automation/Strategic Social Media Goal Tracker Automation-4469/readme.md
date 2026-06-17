## 简介
**Strategic Social Media Goal Tracker Automation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4469

---

# Strategic Social Media Goal Tracker Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| Client Intake Form | Webhook |
| Create SMART Goals | Function |
| Store Client Profile | MongoDB |
| Daily Data Collection | 定时触发器 |
| Get All Clients | MongoDB |
| Split By Client | 分批处理 |
| Has Instagram? | IF 判断 |
| Instagram Data | instagram |
| Has Facebook? | IF 判断 |
| Facebook Data | facebookGraphApi |
| Has LinkedIn? | IF 判断 |
| LinkedIn Data | linkedInCompanies |
| Has Twitter/X? | IF 判断 |
| Twitter/X Data | Twitter |
| Process Performance Data | Function |
| Store Performance Data | MongoDB |
| Check Alert Thresholds | IF 判断 |
| Send Alert Email | Email 发送 |
| Check Milestone Achievements | IF 判断 |
| Send Milestone Email | Email 发送 |
| Monthly Report Trigger | 定时触发器 |
| Get Clients for Reports | MongoDB |
| Split By Client for Reports | 分批处理 |
| Get Client Performance History | MongoDB |
| Generate Monthly Report | Function |
| Create HTML Report | Function |
| Send Monthly Report | Email 发送 |
| Quarterly Strategy Review | 定时触发器 |
| Get Clients for Strategy Review | MongoDB |
| Split By Client for Review | 分批处理 |
| Get Quarterly Performance Data | MongoDB |
| Generate Strategy Review | Function |
| Create Strategy Review Document | Function |
| Send Strategy Review | Email 发送 |
| Content Calendar Webhook | Webhook |
| Get Client for Content Calendar | MongoDB |
| Generate Content Calendar | Function |
| Create Content Calendar HTML | Function |
| Return Content Calendar | 响应 Webhook |



## 功能说明

社交媒体管理，多平台内容发布和监听，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：39
- 触发方式：Webhook 触发

## 触发方式
- Client Intake Form 触发
- Daily Data Collection 触发
- Monthly Report Trigger 触发
- Quarterly Strategy Review 触发
- Content Calendar Webhook 触发

## 统计
- 节点总数：39
- 触发节点：5
- 处理节点：29
- 输出节点：5
- 分类：workflow-automation
