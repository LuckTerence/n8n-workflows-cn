## 简介
**Generate Character-Consistent AI Images with KIE.AI Nano Banana API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8019

---

# Generate Character-Consistent AI Images with KIE.AI Nano Banana API


## 节点清单

| 节点 | 类型 |
|------|------|
| Obtain the generated status | HTTP Request |
| Submit Text Prompt for image Generation | 表单触发器 |
| Send image Generation Request to KIE.AI API | HTTP Request |
| Wait for image Processing Completion | 等待 |
| Check if image Generation is Complete | IF 判断 |
| Format and Display image Results | 数据设置 |

## 触发方式
- Submit Text Prompt for image Generation 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
