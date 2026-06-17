# 精选合集

> 从 1480 个工作流中精选出的场景化推荐组合。按「上手难度」和「实用价值」排序，标注了适配程度（Tier A = 改完就能跑，Tier B = 核心链路通了）。

---

## 🚀 新手入门：从这里开始

如果你是第一次用 n8n，按这个顺序试：

| 顺序 | 工作流 | 说明 | 难度 | 层级 |
|:---:|--------|------|:---:|:---:|
| 1 | [AI Agent聊天](workflows/ai-agent/AI Agent聊天-1954/) | 最基础的 AI 对话 Agent，5 个节点，配好 DeepSeek API Key 就能聊 | ⭐ | A |
| 2 | [Ollama天气查询](workflows/ai-agent/Ollama天气查询-2931/) | 本地 AI + 天气 API，不需要任何云服务账号 | ⭐ | A |
| 3 | [定时启停n8n工作流](workflows/devops/定时启停n8n工作流-3229/) | 学会用 n8n 管理 n8n 本身，按时间表开关工作流 | ⭐ | A |
| 4 | [构建AI自动化](workflows/ai-agent/构建AI自动化-3941/) | 了解如何用 n8n 把 AI 能力嵌入业务流程 | ⭐⭐ | A |

---

## 💬 AI 聊天与客服

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [AI客服中心Telegram呼入](workflows/ai-agent/AI客服中心Telegram呼入-4044/) | 完整的 Telegram 客服机器人，支持呼入自动回复 | Telegram 客服 | A |
| [AI个人助理WhatsApp](workflows/ai-agent/AI个人助理WhatsApp-3947/) | WhatsApp 上的 AI 个人助理 | 个人效率 | B |
| [AI 数据库对话 Agent](workflows/ai-agent/AI 数据库对话 Agent-2612/) | 用自然语言查询数据库，不需要写 SQL | 数据分析 | A |
| [AI 日历助手](workflows/ai-agent/AI 日历助手-2703/) | AI 驱动的日程管理 | 个人效率 | B |

---

## 📧 邮件自动化

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [AI邮件处理+审批](workflows/workflow-automation/AI邮件处理+审批-2861/) | AI 先处理邮件内容，再走人工审批流程 | 企业邮件管理 | B |
| [AI邮件自动回复RAG](workflows/workflow-automation/AI邮件自动回复RAG-4748/) | 基于知识库的智能邮件回复 | 客服邮件 | B |
| [Gmail垃圾邮件清理](workflows/workflow-automation/Gmail垃圾邮件清理-4507/) | 自动识别和清理垃圾邮件 | 邮箱维护 | B |
| [Gmail客服自动回复](workflows/workflow-automation/Gmail客服自动回复-4760/) | Gmail 收到邮件后 AI 自动回复 | 客服自动化 | B |
| [Gmail智能分类归档](workflows/workflow-automation/Gmail智能分类归档-3686/) | AI 自动给邮件打标签、分类、归档 | 邮件整理 | B |
| [人工审核邮件回复](workflows/workflow-automation/人工审核邮件回复-2907/) | AI 生成回复 → 人工审核 → 发送，防出错 | 合规场景 | B |
| [AI邮件附件分析](workflows/multimodal-ai/AI邮件附件分析-3169/) | 自动分析邮件附件内容（图片/文档） | 附件处理 | B |

---

## 📝 内容创作与媒体

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [AI文章摘要生成](workflows/workflow-automation/AI文章摘要生成-2822/) | 输入长文，AI 自动提炼摘要 | 信息处理 | B |
| [AI文章抓取到Notion](workflows/workflow-automation/AI文章抓取到Notion-3535/) | 自动抓取网页文章，AI 整理后存到 Notion | 知识管理 | B |
| [AI新闻简报构建](workflows/workflow-automation/AI新闻简报构建-4030/) | 多源新闻聚合 + AI 摘要 = 每日简报 | 信息聚合 | B |
| [AI新闻研究团队](workflows/workflow-automation/AI新闻研究团队-2778/) | 多 Agent 协作研究新闻话题 | 深度研究 | B |
| [AI图片生成Telegram推送](workflows/multimodal-ai/AI图片生成Telegram推送-4049/) | Telegram 发prompt → AI生图 → 推送回Telegram | 图片生成 | A |
| [fal.ai图片生成](workflows/multimodal-ai/fal.ai图片生成-4108/) | 调用 fal.ai 的 Flux 模型生成高质量图片 | AI 绘图 | A |
| [AI图片敏感内容检测](workflows/multimodal-ai/AI图片敏感内容检测-5661/) | 自动检测上传图片是否包含敏感内容 | 内容审核 | A |
| [Telegram发票识别](workflows/multimodal-ai/Telegram发票识别-4361/) | Telegram 发发票照片 → AI 识别 → 提取结构化信息 | 财务报销 | A |

---

## 🛒 电商运营

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [Shopify弃购挽回](workflows/workflow-automation/Shopify弃购挽回-3415/) | 用户加购未付款 → 自动发挽回邮件/消息 | 电商转化 | B |
| [弃购挽回分析](workflows/workflow-automation/弃购挽回分析-6045/) | 分析弃购原因，AI 给出优化建议 | 电商分析 | B |
| [AI数字产品销售](workflows/workflow-automation/AI数字产品销售-3342/) | 自动化数字产品交付流程 | 数字商品 | B |
| [电商3D视频生成](workflows/multimodal-ai/电商3D视频生成-4987/) | 商品图 → 3D 展示视频 | 商品展示 | B |

---

## 📊 数据、招聘与金融

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [AI简历筛选ERPNext](workflows/workflow-automation/AI简历筛选ERPNext-2757/) | AI 自动筛选简历，结果同步到 ERPNext | 招聘 | A |
| [AI销售线索ERPNext](workflows/workflow-automation/AI销售线索ERPNext-2758/) | AI 分析销售线索，自动录入 CRM | 销售 | A |
| [AI股票基本面分析](workflows/finance-analysis/AI股票基本面分析-2183/) | AI 多维度分析股票基本面数据 | 投资研究 | A |
| [AAVE投资组合Agent](workflows/finance-analysis/AAVE投资组合Agent-4267/) | 加密货币投资组合管理 Agent | 加密投资 | B |
| [AI 技术雷达顾问](workflows/ai-agent/AI 技术雷达顾问-3151/) | AI 追踪技术趋势，生成技术雷达报告 | 技术决策 | A |
| [自适应RAG策略](workflows/knowledge-rag/自适应RAG策略-3459/) | 根据查询复杂度自动切换检索策略的 RAG 系统 | 知识库 | B |

---

## 🔧 DevOps & 运维

| 工作流 | 说明 | 场景 | 层级 |
|--------|------|------|:---:|
| [AI Linux管理员](workflows/devops/AI Linux管理员-3020/) | 用自然语言管理 Linux 服务器 | 运维效率 | A |
| [定时启停n8n工作流](workflows/devops/定时启停n8n工作流-3229/) | 按时间表自动开关工作流 | n8n 管理 | A |
| [多级网页搜索](workflows/ai-agent/多级网页搜索-2539/) | 多轮搜索 + AI 整合结果 | 信息检索 | A |
| [AI网页抓取](workflows/workflow-automation/AI网页抓取-2552/) | AI 辅助的智能网页内容抓取 | 数据采集 | B |

---

## 🎲 好玩的

| 工作流 | 说明 | 层级 |
|--------|------|:---:|
| [3D手办生成](workflows/multimodal-ai/3D手办生成-3628/) | 文字描述 → 3D 模型 | B |

---

## 📈 按场景速查

- **想搭客服机器人** → [AI客服中心Telegram呼入](workflows/ai-agent/AI客服中心Telegram呼入-4044/) + [AI邮件自动回复RAG](workflows/workflow-automation/AI邮件自动回复RAG-4748/)
- **想做邮件自动化** → [AI邮件处理+审批](workflows/workflow-automation/AI邮件处理+审批-2861/) + [Gmail智能分类归档](workflows/workflow-automation/Gmail智能分类归档-3686/)
- **想做内容运营** → [AI新闻简报构建](workflows/workflow-automation/AI新闻简报构建-4030/) + [AI图片生成Telegram推送](workflows/multimodal-ai/AI图片生成Telegram推送-4049/)
- **想做电商增长** → [Shopify弃购挽回](workflows/workflow-automation/Shopify弃购挽回-3415/) + [弃购挽回分析](workflows/workflow-automation/弃购挽回分析-6045/)
- **想做投资研究** → [AI股票基本面分析](workflows/finance-analysis/AI股票基本面分析-2183/) + [AI 技术雷达顾问](workflows/ai-agent/AI 技术雷达顾问-3151/)

---

> 💡 这些工作流大多替换了国内服务（DeepSeek、飞书等），Tier A 的配好 API Key 基本能跑。Tier B 的核心链路通了，边角节点可能需要根据自己的场景调一下。欢迎提 PR 把更多工作流提升到 Tier A。
