## 简介
**Get notified when Meta Ads balance is low**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2936

---

# Get notified when Meta Ads balance is low


## 节点清单

| 节点 | 类型 |
|------|------|
| Every 12h | 定时触发器 |
| No Operation, do nothing | 空操作 |
| Edit Fields1 | 数据设置 |
| Edit Fields | 数据设置 |
| Lower than 400 ? | IF 判断 |
| Send message | Telegram |
| Method 2 | facebookGraphApi |
| Method 1 | facebookGraphApi |

## 触发方式
- Every 12h 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
