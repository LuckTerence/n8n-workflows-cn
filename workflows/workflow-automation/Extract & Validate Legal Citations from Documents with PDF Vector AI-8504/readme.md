## 简介
**Extract & Validate Legal Citations from Documents with PDF Vector AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8504

---

# Extract & Validate Legal Citations from Documents with PDF Vector AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Google Drive - Get Legal Document | Google Drive |
| PDF Vector - Extract Citations | pdfVector |
| Analyze & Validate Citations | Code |
| Has Academic DOIs? | IF 判断 |
| PDF Vector - Fetch Papers | pdfVector |
| Generate Citation Report | Code |
| Save Citation Report | 写入二进制文件 |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
