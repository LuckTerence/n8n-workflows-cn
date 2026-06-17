## 简介
**Simple Lead Capture and Follow-on with n8n Multi-Forms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2581

---

# Simple Lead Capture and Follow-on with n8n Multi-Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| About You | 表单 |
| Your Interests | 表单 |
| Join Beta Testers | 表单 |
| Sign Up Form | 表单触发器 |
| Capture More Info | Google Sheets |
| Capture Email | Google Sheets |
| Show Completion Screen | 表单 |
| Notify New Signup! | Slack |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据（Simple)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：表单提交触发

## 触发方式
- Sign Up Form 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
