## 简介
**Automated Video Translation & Distribution with DubLab to Multiple Platforms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4751

---

# Automated Video Translation & Distribution with DubLab to Multiple Platforms


## 节点清单

| 节点 | 类型 |
|------|------|
| Init Dubbing | HTTP Request |
| Upload Video | HTTP Request |
| Start Dubbing | HTTP Request |
| Fetch Projects | HTTP Request |
| Combine Videos and Languages | Code |
| Proxy Videos | 数据合并 |
| Proxy Ids | 数据合并 |
| Webhook | Webhook |
| Original Video | HTTP Request |
| Dubbed Video | HTTP Request |
| Telegram | Telegram |
| Box | box |
| Dropbox | dropbox |
| YouTube | youTube |
| Postiz | HTTP Request |
| Start | 表单触发器 |



## 功能说明

AI 视频生成工作流，自动创作视频内容，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：16
- 触发方式：Webhook 触发, 表单提交触发

## 触发方式
- Webhook 触发
- Start 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：6
- 输出节点：8
- 分类：workflow-automation
