## 简介
**Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2688

---

# Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!


## 节点清单

| 节点 | 类型 |
|------|------|
| Basic LLM Chain | LLM Chain |
| Google Gemini Chat Model | OpenAI Chat Model |
| Schedule Trigger | 定时触发器 |
| CreateYearsList | Code |
| CleanUpYearList | 数据设置 |
| SplitOutYearList | 数据拆分 |
| GetFrontPage | HTTP Request |
| ExtractDetails | HTML |
| GetHeadlines | 数据设置 |
| GetDate | 数据设置 |
| MergeHeadlinesDate | 数据合并 |
| SingleJson | 数据聚合 |
| Telegram | Telegram |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
