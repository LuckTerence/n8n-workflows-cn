## 简介
**Auto-generate sticky notes and rename nodes**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：22 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/13868

---

# Auto-generate sticky notes and rename nodes


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Parse Nodes | Code |
| AI Groups Logically | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Generate Stickies | Code |
| Strip & Prepare | Code |
| Compute Bounding Boxes | Code |
| Collision Resolution | Code |
| Merge & Export | Code |
| Pick Best Result | Code |
| Collision Detector | Code |
| If | IF 判断 |
| Loop Controller (Automatic Fixer) | Code |
| Set Workflow Variables | 数据设置 |
| Should Rename Nodes | IF 判断 |
| Output Normalization | 数据设置 |
| Parse for Renaming | Code |
| AI Rename | AI Agent |
| Apply Renames | Code |
| Format for Export | Code |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |

## 触发方式
- Start 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：22
- 输出节点：0
- 分类：workflow-automation
