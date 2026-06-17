## 简介
**Route API requests via webhook with retries and backup endpoints**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/16174

---

# Route API requests via webhook with retries and backup endpoints


## 节点清单

| 节点 | 类型 |
|------|------|
| API Recovery Webhook | Webhook |
| Extract Request Configuration | 数据设置 |
| Execute Primary API Request | HTTP Request |
| Check Primary API Success | IF 判断 |
| Return Primary API Response | 响应 Webhook |
| Wait Before Retry Attempt | 等待 |
| Retry Primary API Request | HTTP Request |
| Check Retry API Success | IF 判断 |
| Return Retry API Response | 响应 Webhook |
| Execute Backup API Request | HTTP Request |
| Check Backup API Success | IF 判断 |
| Return Backup API Response | 响应 Webhook |
| Prepare Failure Payload | 数据设置 |
| Return Final Failure Response | 响应 Webhook |

## 触发方式
- API Recovery Webhook 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：6
- 输出节点：7
- 分类：devops
