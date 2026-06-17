## 简介
**Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/5836

---

# Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India


## 节点清单

| 节点 | 类型 |
|------|------|
| Respond to Webhook - Success | 响应 Webhook |
| Respond to Webhook - Error | 响应 Webhook |
| Switch - Check for Success | Switch 路由 |
| DIGIPIN_Generation_Code | Code |
| DIGIPIN_Decode_Code | Code |
| Encode_Webhook | Webhook |
| Decode_Webhook | Webhook |
| Switch 2 - Check for Success1 | Switch 路由 |
| Respond to Webhook - Success 2 | 响应 Webhook |
| Respond to Webhook - Error 2 | 响应 Webhook |

## 触发方式
- Encode_Webhook 触发
- Decode_Webhook 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：4
- 输出节点：4
- 分类：devops
