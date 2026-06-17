## 简介
**Research SEO keywords from a seed term with Keupera and n8n data tables**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15921

---

# Research SEO keywords from a seed term with Keupera and n8n data tables


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait 10s | 等待 |
| Start workflow | 表单触发器 |
| Create a data table | 数据表 |
| Set Seed Keyword | 数据设置 |
| Perform Keyword Research | HTTP Request |
| Poll Keyword Results | HTTP Request |
| Insert row | 数据表 |
| Split Keywords | Code |
| Completed? | IF 判断 |

## 触发方式
- Start workflow 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
