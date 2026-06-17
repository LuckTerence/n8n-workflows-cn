# Bytedance Seedream 3: Text-to-Image Transformation Template

https://n8nworkflows.xyz/workflows/6786

## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Set API Token | 数据设置 |
| Set Image Parameters | 数据设置 |
| Create Image Prediction | HTTP Request |
| Wait 5s | 等待 |
| Check Status | HTTP Request |
| Is Complete? | IF 判断 |
| Has Failed? | IF 判断 |
| Wait 10s | 等待 |
| Success Response | 数据设置 |
| Error Response | 数据设置 |
| Display Result | 数据设置 |
| Log Request | Code |

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：workflow-automation
