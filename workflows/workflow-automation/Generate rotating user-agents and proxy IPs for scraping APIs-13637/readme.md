## 简介
**Generate rotating user-agents and proxy IPs for scraping APIs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13637

---

# Generate rotating user-agents and proxy IPs for scraping APIs


## 节点清单

| 节点 | 类型 |
|------|------|
| user-agents | HTTP Request |
| clean the return to line in user-agent | 数据设置 |
| random sort | 数据排序 |
| Extract user-agent values | HTML |
| Split Out | 数据拆分 |
| Check used IP/user-agent with cloudflare | HTTP Request |
| Manual trigger | 手动触发 |
| SET your proxy connection details here | 数据设置 |
| Merge | 数据合并 |
| Take X random user-agents | 数据限制 |
| Targeted API | HTTP Request |
| IP address and user-agent used | 数据设置 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- Manual trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
