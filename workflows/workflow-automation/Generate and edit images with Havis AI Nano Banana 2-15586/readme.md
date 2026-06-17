## 简介
**Generate and edit images with Havis AI Nano Banana 2**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/15586

---

# Generate and edit images with Havis AI Nano Banana 2


## 节点清单

| 节点 | 类型 |
|------|------|
| Form - Nano Banana 2 | 表单触发器 |
| Build Payload | Code |
| Submit - Havis API | HTTP Request |
| Wait 8s | 等待 |
| Check Task Status | HTTP Request |
| Is Completed? | IF 判断 |
| Is Failed? | IF 判断 |
| Wait 8s (loop) | 等待 |
| Return Result | 数据设置 |
| Return Error | 数据设置 |

## 触发方式
- Form - Nano Banana 2 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
