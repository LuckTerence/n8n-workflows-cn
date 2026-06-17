## 简介
**Create a REST API for PDF Digital Signatures with Webhooks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：25 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/3119

---

# Create a REST API for PDF Digital Signatures with Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Validate Key Gen Params | Code |
| Validate PDF Sign Params | Code |
| Validate PDF Upload | Code |
| Validate Key Upload | Code |
| Generate Keys | Code |
| Sign PDF | Code |
| Prepare Success Response | 数据设置 |
| Switch Operation | Switch 路由 |
| Switch Upload Type | Switch 路由 |
| Prepare input params | 数据设置 |
| set file path | 数据设置 |
| Convert PDF to File | 转换为文件 |
| Write PDF File to Disk | 读写文件 |
| Read PDF File from Disk | 读写文件 |
| Convert PFX to File | 转换为文件 |
| Write PFX File to Disk | 读写文件 |
| Read PFX File from Disk | 读写文件 |
| Check PDF file is OK | 数据设置 |
| Check PFX file is OK | 数据设置 |
| check success | IF 判断 |
| set downlowd file info | 数据设置 |
| Read download file from Disk | 读写文件 |
| API POST Endpoint | Webhook |
| API GET Endpoint | Webhook |
| POST Success Response | 响应 Webhook |
| POST Error Response | 响应 Webhook |
| GET Respond to Webhook | 响应 Webhook |

## 触发方式
- API POST Endpoint 触发
- API GET Endpoint 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：22
- 输出节点：3
- 分类：workflow-automation
