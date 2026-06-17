## 简介
**Magento 2: Auto-Fix Missing Image Alt Tags with Product Name**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/6715

---

# Magento 2: Auto-Fix Missing Image Alt Tags with Product Name


## 节点清单

| 节点 | 类型 |
|------|------|
| Get All Product Skus | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| If | IF 判断 |
| Code | Code |
| Split Out | 数据拆分 |
| HTTP Request | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
