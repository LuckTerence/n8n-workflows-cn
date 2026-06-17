## 简介
**Bulk Email Validation and AI Scoring with ZeroBounce**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11538

---

# Bulk Email Validation and AI Scoring with ZeroBounce


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Low score | 空操作 |
| Not valid | 空操作 |
| Is valid? | Switch 路由 |
| Sandbox emails | 数据设置 |
| Filter by score | Switch 路由 |
| Medium score | 空操作 |
| High score | 空操作 |
| Send file for validation | zeroBounce |
| Wait for validation file to be processed | 等待 |
| Get validation results file | zeroBounce |
| Get validation file status | zeroBounce |
| Send file for scoring | zeroBounce |
| Get scoring file status | zeroBounce |
| Get scoring results file | zeroBounce |
| Wait for scoring file to process | 等待 |
| Merge validation and scoring results | 数据合并 |
| Scoring file status | Switch 路由 |
| Validation file status | Switch 路由 |
| Validation results | 空操作 |
| Bulk validation failed | 停止并报错 |
| Bulk scoring failed | 停止并报错 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 实现自动化。

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

- 节点总数：22
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：21
- 输出节点：0
- 分类：workflow-automation
