## 简介
**Automate Docker-based n8n Updates with Email Approval and SSH**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10471

---

# Automate Docker-based n8n Updates with Email Approval and SSH


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| If No Changes | IF 判断 |
| Check Existence of Update Script | SSH |
| If File Exists | IF 判断 |
| Create Update Script | SSH |
| If Approved | IF 判断 |
| No Updates | 空操作 |
| Do Nothing | 空操作 |
| Ask For Approval to Update | Email 发送 |
| Execute Update Script | SSH |
| Get Local Image Digest | SSH |
| Get Remote Image Digest | HTTP Request |
| Prepare Update Data | 数据设置 |
| Get Current n8n Version | SSH |



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

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：devops
