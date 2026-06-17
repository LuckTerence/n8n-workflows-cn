## 简介
**Ingest and enrich Q&A pairs then store in Data Table [1-2]**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13353

---

# Ingest and enrich Q&A pairs then store in Data Table [1-2]


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| is n8n.io email? | IF 判断 |
| isTrusted:true | 数据设置 |
| isTrusted:false | 数据设置 |
| ref | 空操作 |
| OpenAI Chat Model | OpenAI Chat Model |
| Add tags | LLM Chain |
| Insert row | 数据表 |



## 功能说明

Ingest and enrich Q&A pairs then store in Data Tab（AI 增强)表单提交触发，通过 邮箱 实现自动化。

，通过 邮箱 实现自动化。

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

- 节点总数：8
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
