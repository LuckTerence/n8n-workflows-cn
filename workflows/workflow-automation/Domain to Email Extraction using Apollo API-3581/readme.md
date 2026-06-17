## 简介
**Domain to Email Extraction using Apollo API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3581

---

# Domain to Email Extraction using Apollo API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Targets | 分批处理 |
| Pull Target Domains | Google Sheets |
| Get People By Domain | HTTP Request |
| Clean Up Results | Code |
| Loop Over Results | 分批处理 |
| Get Person Info | HTTP Request |
| Clean Up | Code |
| Results To Results Sheet | Google Sheets |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
