## 简介
**Automate Droplet Snapshots on DigitalOcean**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2485

---

# Automate Droplet Snapshots on DigitalOcean


## 节点清单

| 节点 | 类型 |
|------|------|
| Filter | 过滤器 |
| List Snapshots for a Droplet | HTTP Request |
| List All Droplets | HTTP Request |
| Delete a Snapshot | HTTP Request |
| Droplet Actions snapshot (n8n.optimus01.co.za) | HTTP Request |
| Runs every 48hrs | 定时触发器 |

## 触发方式
- Runs every 48hrs 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：1
- 输出节点：4
- 分类：workflow-automation
