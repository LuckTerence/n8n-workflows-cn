# Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India

https://n8nworkflows.xyz/workflows/5836

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
