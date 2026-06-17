## 简介
**Learn API Fundamentals with an Interactive Hands-On Tutorial Workflow**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/5171

---

# Learn API Fundamentals with an Interactive Hands-On Tutorial Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Tutorial | 手动触发 |
| 1. The Kitchen (GET /menu) | Webhook |
| Respond with Menu | 数据设置 |
| 1. The Customer (GET Menu Item) | HTTP Request |
| 2. The Customer (GET with Query Params) | HTTP Request |
| 2. The Kitchen (GET /order) | Webhook |
| Respond with Cheese | 数据设置 |
| Respond with Plain | 数据设置 |
| 3. The Customer (POST with Body) | HTTP Request |
| 3. The Kitchen (POST /review) | Webhook |
| Respond to Review | 数据设置 |
| 4. The Customer (GET with Headers/Auth) | HTTP Request |
| 4. The Kitchen (GET /secret-dish) | Webhook |
| Respond with Secret | 数据设置 |
| Respond with Error | 数据设置 |
| 5. The Customer (Request with Timeout) | HTTP Request |
| 5. The Kitchen (GET /slow-service) | Webhook |
| Respond Slowly | 数据设置 |
| Wait 3 seconds | 等待 |
| Base URL | 数据设置 |
| IF Authorized | IF 判断 |
| IF extra cheese | IF 判断 |

## 触发方式
- Start Tutorial 触发
- 1. The Kitchen (GET /menu) 触发
- 2. The Kitchen (GET /order) 触发
- 3. The Kitchen (POST /review) 触发
- 4. The Kitchen (GET /secret-dish) 触发
- 5. The Kitchen (GET /slow-service) 触发

## 统计
- 节点总数：22
- 触发节点：6
- 处理节点：11
- 输出节点：5
- 分类：devops
