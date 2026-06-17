## 简介
**Build Academic Citation Networks with PDF Vector API for Gephi Visualization**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7356

---

# Build Academic Citation Networks with PDF Vector API for Gephi Visualization


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Parameters | 数据设置 |
| Split Paper IDs | Code |
| PDF Vector - Fetch Papers | pdfVector |
| Fetch Citing Papers | pdfVector |
| Build Network Data | Code |
| Combine Network | Code |
| Export Network JSON | 写入二进制文件 |
| Generate GEXF | Code |

## 触发方式
- 手动触发

## 统计
- 节点总数：8
- 触发节点：0
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
