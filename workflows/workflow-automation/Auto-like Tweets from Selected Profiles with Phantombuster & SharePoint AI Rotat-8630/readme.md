## 简介
**Auto-like Tweets from Selected Profiles with Phantombuster & SharePoint AI Rotation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8630

---

# Auto-like Tweets from Selected Profiles with Phantombuster & SharePoint AI Rotation


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait1 | 等待 |
| Get Random Post | Code |
| Create CSV Binary | Code |
| Upload CSV | SharePoint |
| Get Response | phantombuster |
| Get Autoliking Agent | phantombuster |
| Launch AL Agent | phantombuster |
| Set ENV Variables | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Update file | SharePoint |
| Download file | SharePoint |
| Check if in List | Code |
| If | IF 判断 |
| Wait2 | 等待 |
| Prepare Updated Data | Code |
| Extract from File | 从文件提取 |
| Convert to File | 转换为文件 |
| Get Available Session Cookies | SharePoint |
| Extract Cookies | 从文件提取 |
| Select Cookie | AI Agent |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Get Profile Extractor Agent | phantombuster |
| Get List of Accounts | SharePoint |
| If Empty | IF 判断 |
| HTTP Request | HTTP Request |
| HTTP Request1 | HTTP Request |
| Prepare Posts | Code |
| Wait3 | 等待 |
| Launch Agent1 | phantombuster |



## 功能说明

文件处理工具，自动转换或管理文件，定时执行。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：29
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：26
- 输出节点：2
- 分类：workflow-automation
