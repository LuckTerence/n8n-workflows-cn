## 简介
**Generate Research Ideas from PDFs using InfraNodus GraphRAG Content Gap Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5746

---

# Generate Research Ideas from PDFs using InfraNodus GraphRAG Content Gap Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Convert File to PDF | HTTP Request |
| On form submission | 表单触发器 |
| Convert binary files to PDF | Code |
| Extract text from PDF files | 从文件提取 |
| Prepare for InfraNodus | Code |
| Display on the Form to the User | 表单 |
| InfraNodus GraphRAG Question Generator | HTTP Request |
| InfraNodus GraphRAG Response Generator | HTTP Request |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
