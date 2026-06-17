## 简介
**MFA Multi-factor authentication (Voice call and Email) with ClickSend and SMTP**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3142

---

# MFA Multi-factor authentication (Voice call and Email) with ClickSend and SMTP


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Voice | HTTP Request |
| On form submission | 表单触发器 |
| Send Email | Email 发送 |
| Code for voice | Code |
| Set voice code | 数据设置 |
| Verify voice code | 表单 |
| Fail voice code | 表单 |
| Set email code | 数据设置 |
| Verify email code | 表单 |
| Is email code correct? | IF 判断 |
| Is voice code correct? | IF 判断 |
| Success | 表单 |
| Fail email code | 表单 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：multimodal-ai
