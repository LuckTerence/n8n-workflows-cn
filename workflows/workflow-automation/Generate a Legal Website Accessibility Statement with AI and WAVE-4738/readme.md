## 简介
**Generate a Legal Website Accessibility Statement with AI and WAVE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4738

---

# Generate a Legal Website Accessibility Statement with AI and WAVE


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Website HTML | HTTP Request |
| Get WAVE Report | HTTP Request |
| Structured Output Parser | 结构化输出解析器 |
| Accessibility Statement Generator | AI Agent |
| gemini 2.5 pro | OpenAI Chat Model |
| Parse output as html | HTML |
| Create accesibility statement html file | moveBinaryData |
| Map WAVE Report Items to Website selectors. | Code |
| CHANGE THESE: dependencies | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Send accessibility statement by email | Email 发送 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
