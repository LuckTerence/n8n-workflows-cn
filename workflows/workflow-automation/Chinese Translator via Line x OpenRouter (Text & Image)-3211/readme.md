## 简介
**Chinese Translator via Line x OpenRouter (Text & Image)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3211

---

# Chinese Translator via Line x OpenRouter (Text & Image)


## 节点清单

| 节点 | 类型 |
|------|------|
| Line Webhook | Webhook |
| Line Loading Animation | HTTP Request |
| Switch | Switch 路由 |
| Get Image | HTTP Request |
| OpenRouter : qwen/qwen2.5-vl-72b-instruct:free | HTTP Request |
| OpenRouter: qwen/qwen-2.5-72b-instruct:free | HTTP Request |
| Extract from File | 从文件提取 |
| Line Reply (image) | HTTP Request |
| Line Reply (Text) | HTTP Request |
| Line Reply (Not Supported 2) | HTTP Request |
| Line Reply (Not Supported 1) | HTTP Request |

## 触发方式
- Line Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：2
- 输出节点：8
- 分类：workflow-automation
