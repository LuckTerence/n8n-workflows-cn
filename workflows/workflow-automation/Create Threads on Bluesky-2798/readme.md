## 简介
**Create Threads on Bluesky**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2798

---

# Create Threads on Bluesky


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Bluesky Session | HTTP Request |
| Create Reply | HTTP Request |
| Run Daily at 9 AM | 定时触发器 |
| Set Bluesky Credentials | 数据设置 |
| Create Reply Text | Code |
| Create Sibling Text | Code |
| Create Sibling | HTTP Request |
| Loop Posts | 分批处理 |
| Create Initial Post | HTTP Request |
| Create Post | HTTP Request |
| Wait | 等待 |
| Create Post Text | Code |
| Create Sibling Array | Code |
| Create Sibling Text (Loop) | Code |

## 触发方式
- Run Daily at 9 AM 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：workflow-automation
