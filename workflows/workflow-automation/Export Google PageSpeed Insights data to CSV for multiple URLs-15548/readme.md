## 简介
**Export Google PageSpeed Insights data to CSV for multiple URLs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15548

---

# Export Google PageSpeed Insights data to CSV for multiple URLs


## 节点清单

| 节点 | 类型 |
|------|------|
| Parse & Normalise URLs | Code |
| Early Exit Check | IF 判断 |
| Respond - No Valid URLs | Code |
| Split Valid URLs | 列表操作 |
| Reachability Check | HTTP Request |
| Filter Reachable | Code |
| Second Early Exit | IF 判断 |
| Split Reachable URLs | 列表操作 |
| Loop | 分批处理 |
| PageSpeed API | HTTP Request |
| Extract PageSpeed Data | Code |
| Upload to Uguu | HTTP Request |
| Respond to Chat | 聊天 |
| When chat message received | Chat 触发器 |
| Wait | 等待 |
| Convert to File | 转换为文件 |
| Aggregate | 数据聚合 |
| Extract Link | Code |
| Final Chat | 聊天 |



## 功能说明

Export Google PageSpeed Insights data to CSV for m（AI 增强)Chat 消息触发，通过 HTTP API 实现自动化。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：19
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：13
- 输出节点：5
- 分类：workflow-automation
