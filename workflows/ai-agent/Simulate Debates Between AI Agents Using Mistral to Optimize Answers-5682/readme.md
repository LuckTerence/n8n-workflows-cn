## 简介
**Simulate Debates Between AI Agents Using Mistral to Optimize Answers**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5682

---

# Simulate Debates Between AI Agents Using Mistral to Optimize Answers


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule | 定时触发器 |
| Configure Workflow Args | globalConstants |
| When clicking ‘Execute workflow’ | 手动触发 |
| Email Trigger (IMAP) | Email 读取 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Simple Memory | 记忆缓冲区 |
| Prepare Input | 数据设置 |
| Update Input | 数据设置 |
| Split Out AI Agents | 数据拆分 |
| JSON Output Parser | 结构化输出解析器 |
| If No More Rounds | IF 判断 |
| End of Debate | 空操作 |
| Debate Loop | 分批处理 |
| Round Loop | 分批处理 |
| Debate Actor Abstraction | AI Agent |
| Debate Environment | AI Agent |
| Guarantee Input | 数据设置 |
| Mistral Cloud Chat Model 2 | Mistral Chat Model |
| Aggregate | 数据聚合 |
| JSON Output Parser 2 | 结构化输出解析器 |
| Simple Memory 2 | 记忆缓冲区 |
| Wait Before Sending Agents | 等待 |
| Wait 1 | 等待 |
| Wait 2 | 等待 |



## 功能说明

Simulate Debates Between AI Agents Using Mistral t（AI 增强)定时触发、手动触发，通过 邮箱 实现自动化。

定时触发、手动触发，通过 邮箱 实现自动化。

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

- 节点总数：24
- 触发方式：定时触发, 手动触发

## 触发方式
- Schedule 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：21
- 输出节点：1
- 分类：ai-agent
