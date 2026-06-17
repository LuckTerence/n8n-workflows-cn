## 简介
**Check Which AI Models Are Used in Your Workflows**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3718

---

# Check Which AI Models Are Used in Your Workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Edit Fields-set_model_data | 数据设置 |
| Google Sheets-Clear Sheet Data | Google Sheets |
| n8n-get all workflow | n8n |
| Filter-get workflow contain modelid | 过滤器 |
| Split Out-nodes | 数据拆分 |
| Filter-node contain modelId | 过滤器 |
| Google Sheets-Save node and workflow data | Google Sheets |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
