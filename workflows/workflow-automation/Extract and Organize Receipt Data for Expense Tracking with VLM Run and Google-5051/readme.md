## 简介
**Extract and Organize Receipt Data for Expense Tracking with VLM Run and Google**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/5051

---

# Extract and Organize Receipt Data for Expense Tracking with VLM Run and Google


## 节点清单

| 节点 | 类型 |
|------|------|
| Monitor Receipt Uploads | Google Drive 触发器 |
| Download  Receipt File | Google Drive |
| VLM Run Receipt Parser | vlmRun |
| Format Receipt Data | 数据设置 |
| Save to Expense Database | Google Sheets |

## 触发方式
- Monitor Receipt Uploads 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：4
- 输出节点：0
- 分类：workflow-automation
