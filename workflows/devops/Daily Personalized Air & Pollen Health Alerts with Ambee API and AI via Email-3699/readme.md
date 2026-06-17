## 简介
**Daily Personalized Air & Pollen Health Alerts with Ambee API and AI via Email**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3699

---

# Daily Personalized Air & Pollen Health Alerts with Ambee API and AI via Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Air data | HTTP Request |
| Get Pollen data | HTTP Request |
| AI Agent | AI Agent |
| Think | 思考工具 |
| OpenAI Chat Model | OpenAI Chat Model |
| Gmail | Gmail 工具 |
| Schedule Trigger | 定时触发器 |
| Set Your Location Coordinates | 数据设置 |
| Set User Profile | 数据设置 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：devops
