## 简介
**Generate AI Stock Reports w- Fundamental, Technical, & News Analysis (Free APIs)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11772

---

# Generate AI Stock Reports w- Fundamental, Technical, & News Analysis (Free APIs)


## 节点清单

| 节点 | 类型 |
|------|------|
| Window Buffer Memory | 记忆缓冲区 |
| AI Agent | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Generate HTML | HTML |
| Adjust HTML Colors | Code |
| Think | 思考工具 |
| Technical Analysis Tool | 工作流工具 |
| Trends Analysis Tool | 工作流工具 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Buy? | IF 判断 |
| Buy in Alpaca | HTTP Request |
| Send Stock Analysis | Email 发送 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Fundamental Analysis Tool | 工作流工具 |
| Get Chart URL | HTTP Request |
| Get Price History | HTTP Request |
| Get Bollinger Bands | HTTP Request |
| Get MACD | HTTP Request |
| Merge | 数据合并 |
| Calculate Support Resistance | Code |
| Organizing Data | Code |
| Merge-2 | 数据合并 |
| ChatGPT 4o | OpenAI |
| Set Variable | 数据设置 |
| Warp as JSON for GPT | Code |
| Set Final Response | 数据设置 |
| Set Stock Symbol and API Key | 数据设置 |
| First Technical Analysis | OpenAI |
| Test NASDAQ | HTTP Request |
| Set exchange to NASDAQ | 数据设置 |
| Test NYSE | HTTP Request |
| Set exchange to NYSE | 数据设置 |
| Stop and Error | 停止并报错 |
| Merge1 | 数据合并 |
| is on nasdaq? | IF 判断 |
| is on NYSE? | IF 判断 |
| Set Variables | 数据设置 |
| Get Company Overview | HTTP Request |
| Get Income Statement | HTTP Request |
| Get Balance Sheet | HTTP Request |
| Code in JavaScript | Code |
| Merge2 | 数据合并 |
| ChatGPT 4o1 | OpenAI |
| Generate Variables For API | Code |
| Get News Data | HTTP Request |
| Analyse API Input | Code |
| Set Variables1 | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Stock List | 数据设置 |
| Wait | 等待 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Set Ticker for AI Agent | 数据设置 |
| On form submission | 表单触发器 |
| If | IF 判断 |
| Execute Workflow | 执行工作流 |
| Wait1 | 等待 |
| Wait2 | 等待 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

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

- 节点总数：58
- 触发方式：定时触发, 表单提交触发

## 触发方式
- When Executed by Another Workflow 触发
- Schedule Trigger 触发
- On form submission 触发

## 统计
- 节点总数：58
- 触发节点：3
- 处理节点：43
- 输出节点：12
- 分类：workflow-automation
