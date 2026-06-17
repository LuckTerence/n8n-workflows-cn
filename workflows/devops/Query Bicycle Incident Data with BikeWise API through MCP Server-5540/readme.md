# Query Bicycle Incident Data with BikeWise API through MCP Server

https://n8nworkflows.xyz/workflows/5540

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
