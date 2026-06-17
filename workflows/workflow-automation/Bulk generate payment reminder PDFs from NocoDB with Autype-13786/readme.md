## 简介
**Bulk generate payment reminder PDFs from NocoDB with Autype**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13786

---

# Bulk generate payment reminder PDFs from NocoDB with Autype


## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Schedule | 定时触发器 |
| Get Overdue Invoices | NocoDB |
| Build Bulk Items | Code |
| Bulk Render Payment Reminders | autype |
| Send ZIP via Email | Email 发送 |
| Run Setup Once | 手动触发 |
| Create Project | autype |
| Create Document | autype |



## 功能说明

财务自动化，发票处理或支付流程管理，定时执行。

定时触发、手动触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：定时触发, 手动触发

## 触发方式
- Weekly Schedule 触发
- Run Setup Once 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
