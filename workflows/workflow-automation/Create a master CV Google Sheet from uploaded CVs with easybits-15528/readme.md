## 简介
**Create a master CV Google Sheet from uploaded CVs with easybits**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15528

---

# Create a master CV Google Sheet from uploaded CVs with easybits


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Split: Experiences | 数据拆分 |
| Append: Experiences | Google Sheets |
| Split: Education | 数据拆分 |
| Append: Education | Google Sheets |
| Split: Skills | 数据拆分 |
| Append: Skills | Google Sheets |
| Append: Summary | Google Sheets |
| Fan-out | Code |
| easybits: Extract CV | easybitsExtractor |
| Wait for All Branches | 数据合并 |
| Show Completion Screen | 表单 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
