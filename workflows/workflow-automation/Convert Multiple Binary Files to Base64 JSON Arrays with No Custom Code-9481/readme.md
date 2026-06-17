## 简介
**Convert Multiple Binary Files to Base64 JSON Arrays with No Custom Code**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9481

---

# Convert Multiple Binary Files to Base64 JSON Arrays with No Custom Code


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Unzip Demo Website | compression |
| Download Demo Website | HTTP Request |
| Split Out Files | 数据拆分 |
| Encode Files to Base64 | 从文件提取 |
| Add Path to Files | 数据设置 |
| Aggregate Output | 数据聚合 |

## 触发方式
- Start 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
