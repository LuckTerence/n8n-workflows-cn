# Automate Actions After PDF Generation with PDFMonkey

https://n8nworkflows.xyz/workflows/3060

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
