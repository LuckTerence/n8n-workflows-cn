## 简介
**Send Postcards to Contacts Automatically using CentralStationCRM and EchtPost**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6124

---

# Send Postcards to Contacts Automatically using CentralStationCRM and EchtPost


## 节点清单

| 节点 | 类型 |
|------|------|
| Person is updated in CentralStationCRM | Webhook |
| Set fields needed for EchtPost | 数据设置 |
| Is "EchtPost" included in "taggings"? | IF 判断 |
| Do nothing | 空操作 |
| Send postcard with EchtPost | HTTP Request |

## 触发方式
- Person is updated in CentralStationCRM 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
