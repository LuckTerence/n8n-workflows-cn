## 简介
**Generate AI Videos from Text Prompts with KIE.AI Veo3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/6047

---

# Generate AI Videos from Text Prompts with KIE.AI Veo3


## 节点清单

| 节点 | 类型 |
|------|------|
| Submit Text Prompt for Video Generation | 表单触发器 |
| Send Video Generation Request to KIE.AI API | HTTP Request |
| Wait for Video Processing Completion | 等待 |
| Obtain the generated status | HTTP Request |
| Check if Video Generation is Complete | IF 判断 |
| Format and Display Video Results | 数据设置 |

## 触发方式
- Submit Text Prompt for Video Generation 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
