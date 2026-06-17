## 简介
**Generate Stock Market Insights with Technical Analysis, AI, and Telegram Publishing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8094

---

# Generate Stock Market Insights with Technical Analysis, AI, and Telegram Publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Schedule Trigger | 定时触发器 |
| Execute Auth Login | 执行工作流 |
| Execute Auth Trade API | 执行工作流 |
| Telegram Trigger | Telegram 触发器 |
| Ошибка публикации | Telegram |
| Успешно опубликовано | Telegram |
| Structured Output Parser | 结构化输出解析器 |
| Get Action Type | 数据设置 |
| Exist type and id | IF 判断 |
| Get Post By Id | PostgreSQL |
| Ошибка генерации | Telegram |
| Исторические данные | HTTP Request |
| Рассчет TA | Code |
| ID Generation | 加密 |
| Отправка поста на валидацию | Telegram |
| Публикация постав в Профите | HTTP Request |
| Развилка | Switch 路由 |
| Собираем пост | Code |
| Send a text message | Telegram |
| Сохранение поста | PostgreSQL |
| Данные для анализа (тут указываются ticker) | Code |
| Query callback | Telegram |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：定时触发, Telegram 消息触发

## 触发方式
- Schedule Trigger 触发
- Telegram Trigger 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：14
- 输出节点：8
- 分类：workflow-automation
