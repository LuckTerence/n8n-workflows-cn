## 简介
**Merge Multiple Excel Files into a Single Multi-Sheet File with Summary Page**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8373

---

# Merge Multiple Excel Files into a Single Multi-Sheet File with Summary Page


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Read each XLXS | 分批处理 |
| Read XLXS Files from Disk | 读写文件 |
| Create Multi-Sheet Excel | Code |
| Collect and Process Data | Code |
| Save XLXS to Disk | 读写文件 |
| XLSX to Json List | 从文件提取 |
| Mulipte Json to Single Json | 数据聚合 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
