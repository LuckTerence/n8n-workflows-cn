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

## 触发方式
- Schedule Trigger 触发
- Telegram Trigger 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：14
- 输出节点：8
- 分类：workflow-automation
