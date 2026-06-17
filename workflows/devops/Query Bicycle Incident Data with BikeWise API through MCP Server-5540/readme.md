## 简介
**Query Bicycle Incident Data with BikeWise API through MCP Server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5540

---

# Query Bicycle Incident Data with BikeWise API through MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| BikeWise API v2 MCP Server | MCP 触发器 |
| Paginated incidents matching parameters | HTTP Request 工具 |
| Get incident | HTTP Request 工具 |
| Unpaginated geojson response | HTTP Request 工具 |
| Unpaginated geojson response with simplestyled markers | HTTP Request 工具 |

## 触发方式
- BikeWise API v2 MCP Server 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：0
- 输出节点：4
- 分类：devops
