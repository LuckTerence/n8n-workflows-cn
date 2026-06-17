## 简介
**Generate a Legal Website Accessibility Statement with AI and WAVE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4738

---

# Generate a Legal Website Accessibility Statement with AI and WAVE


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Website HTML | HTTP Request |
| Get WAVE Report | HTTP Request |
| Structured Output Parser | 结构化输出解析器 |
| Accessibility Statement Generator | AI Agent |
| gemini 2.5 pro | OpenAI Chat Model |
| Parse output as html | HTML |
| Create accesibility statement html file | moveBinaryData |
| Map WAVE Report Items to Website selectors. | Code |
| CHANGE THESE: dependencies | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Send accessibility statement by email | Email 发送 |



## 功能说明

Generate a Legal Website Accessibility Statement w（AI 增强)手动触发，通过 邮箱 + HTTP API 实现自动化。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
