## 简介
**Generate AI Music with Suno V3.5 using KIE.ai API and Form Interface**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6046

---

# Generate AI Music with Suno V3.5 using KIE.ai API and Form Interface


## 节点清单

| 节点 | 类型 |
|------|------|
| Submit Music Generation Parameters | 表单触发器 |
| Send Music Generation Request to KIE.ai API | HTTP Request |
| Wait for Music Processing | 等待 |
| Poll Music Generation Status | HTTP Request |
| Check if Music Generation Complete | IF 判断 |
| Format and Display Music Results | 数据设置 |

## 触发方式
- Submit Music Generation Parameters 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：devops
