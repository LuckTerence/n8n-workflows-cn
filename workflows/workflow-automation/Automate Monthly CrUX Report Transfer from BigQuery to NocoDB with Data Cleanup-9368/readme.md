## 简介
**Automate Monthly CrUX Report Transfer from BigQuery to NocoDB with Data Cleanup**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9368

---

# Automate Monthly CrUX Report Transfer from BigQuery to NocoDB with Data Cleanup


## 节点清单

| 节点 | 类型 |
|------|------|
| Google BigQuery | Google BigQuery |
| Get Last Month Data | NocoDB |
| Delete in NocoDB | NocoDB |
| Loop Over Items | 分批处理 |
| Append Crux Data into NocoDB | NocoDB |
| Convert month name to number | Code |
| Edit Fields | 数据设置 |
| Monthly Trigger1 | 定时触发器 |
| Monthly Trigger2 | 定时触发器 |

## 触发方式
- Monthly Trigger1 触发
- Monthly Trigger2 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
