# Ingest and enrich Q&A pairs then store in Data Table [1-2]

https://n8nworkflows.xyz/workflows/13353

## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| is n8n.io email? | IF 判断 |
| isTrusted:true | 数据设置 |
| isTrusted:false | 数据设置 |
| ref | 空操作 |
| OpenAI Chat Model | OpenAI Chat Model |
| Add tags | LLM Chain |
| Insert row | 数据表 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
