## 简介
**Get Taobao and Tmall shop products and first product details with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15867

---

# Get Taobao and Tmall shop products and first product details with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Set API and Shop Parameters | 数据设置 |
| Fetch Shop Product List via API | HTTP Request |
| Store Raw Product List Data | 数据设置 |
| Extract First Product ID | Code |
| Store Extracted Product ID | 数据设置 |
| Fetch Product Details via API | HTTP Request |
| Build Product Detail Output | Code |
| Store Final Product Details | 数据设置 |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
