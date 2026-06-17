## 简介
**Gmail智能分类归档**

AI自动分类邮件并归档

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3686

---

# Gmail智能分类归档


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Telegram Trigger | Telegram 触发器 |
| mail_label_setter | Gmail 工具 |
| mail_archiver | Gmail 工具 |
| Aggregate | 数据聚合 |
| Telegram | Telegram |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Reporter | AI Agent |
| Get mails in INBOX | Gmail |
| Filter processed | 过滤器 |
| Categoriser | AI Agent |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Telegram Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
