## 简介
**N8N Contact Form Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4337

---

# N8N Contact Form Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Redirect Form | 表单 |
| Confirmation Form | 表单 |
| If Email Sent | IF 判断 |
| Send Email to Support | Email 发送 |
| Form | 表单 |
| End (Success) | 空操作 |
| End (Error) | 空操作 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Contact)表单提交触发，通过 邮箱 实现自动化。

，通过 邮箱 实现自动化。

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
- On form submission 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
