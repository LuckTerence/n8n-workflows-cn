## 简介
**Narrative Chaining: AI-Generated Video Scene Extensions with Veo3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：27 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9145

---

# Narrative Chaining: AI-Generated Video Scene Extensions with Veo3


## 节点清单

| 节点 | 类型 |
|------|------|
| Think | 思考工具 |
| GPT | OpenAI Chat Model |
| Analyze Video | HTTP Request |
| Get Analysis | HTTP Request |
| Looper | 数据设置 |
| If  | IF 判断 |
| Combine Clips | HTTP Request |
| Get Final Video | HTTP Request |
| Aggregate | 数据聚合 |
| Get input | Google Sheets |
| Initial Values | 数据设置 |
| Request last | HTTP Request |
| Get last | HTTP Request |
| Get Video | HTTP Request |
| Create Video | HTTP Request |
| Add scene | Google Sheets |
| Increment step | 数据设置 |
| If complete | IF 判断 |
| ExtendRobo AI Agent | AI Agent |
| Wait 2 | 等待 |
| Wait 1 | 等待 |
| Wait  | 等待 |
| Get scenes | Google Sheets |
| Wait 3 | 等待 |
| Update log | Google Sheets |
| Structured Output | 结构化输出解析器 |
| Execute | 手动触发 |
| Clear scenes | Google Sheets |

## 触发方式
- Execute 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：19
- 输出节点：8
- 分类：workflow-automation
