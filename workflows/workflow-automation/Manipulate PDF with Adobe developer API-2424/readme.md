## 简介
**Manipulate PDF with Adobe developer API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2424

---

# Manipulate PDF with Adobe developer API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Create Asset | HTTP Request |
| Execute Workflow Trigger | 执行工作流触发器 |
| Adobe API Query | 数据设置 |
| Load a test pdf file | dropbox |
| Query + File | 数据合并 |
| Query + File + Asset information | 数据合并 |
| Process Query | HTTP Request |
| Wait 5 second | 等待 |
| Try to download the result | HTTP Request |
| Switch | Switch 路由 |
| Forward response to origin workflow | 数据设置 |
| Authenticartion (get token) | HTTP Request |
| Upload PDF File (asset) | HTTP Request |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
