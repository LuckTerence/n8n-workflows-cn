## 简介
**Generate AI Images with Text Prompts using BananaAPI and Nano Banana Engine**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8375

---

# Generate AI Images with Text Prompts using BananaAPI and Nano Banana Engine


## 节点清单

| 节点 | 类型 |
|------|------|
| Form — Get Prompt | 表单触发器 |
| Submit — Banana API | HTTP Request |
| Wait 5s | 等待 |
| Check Status | HTTP Request |
| Wait 5s (loop) | 等待 |
| Return Links | 数据设置 |
| If | IF 判断 |

## 触发方式
- Form — Get Prompt 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：devops
