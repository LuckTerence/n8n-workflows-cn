## 简介
**Automated Indonesian Weather Alerts with BMKG Data & Telegram Notifications**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9675

---

# Automated Indonesian Weather Alerts with BMKG Data & Telegram Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get BMKG Weather Data | HTTP Request |
| Process Weather Data | Code |
| Format Telegram Message | Code |
| Send Weather Report | Telegram |
| Manual Test | 手动触发 |
| Check Success | IF 判断 |
| Error Handler | Code |
| Send Error Alert | Telegram |

## 触发方式
- Schedule Trigger 触发
- Manual Test 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：4
- 输出节点：3
- 分类：devops
