## 简介
**Automate Actions After PDF Generation with PDFMonkey**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：2 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/3060

---

# Automate Actions After PDF Generation with PDFMonkey


## 节点清单

| 节点 | 类型 |
|------|------|
| On PDFMonkey generation process end | Webhook |
| Check if generation was successful | IF 判断 |
| On success: download the PDF file | HTTP Request |

## 触发方式
- On PDFMonkey generation process end 触发

## 统计
- 节点总数：3
- 触发节点：1
- 处理节点：1
- 输出节点：1
- 分类：workflow-automation
