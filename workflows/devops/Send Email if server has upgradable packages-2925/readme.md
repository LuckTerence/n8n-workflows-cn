## 简介
**Send Email if server has upgradable packages**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/2925

---

# Send Email if server has upgradable packages


## 节点清单

| 节点 | 类型 |
|------|------|
| List upgradable packages | SSH |
| Send Email through SMTP | Email 发送 |
| Run workflow every day | 定时触发器 |
| Format as HTML list | Code |
| Check if there are updates | IF 判断 |

## 触发方式
- Run workflow every day 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：devops
