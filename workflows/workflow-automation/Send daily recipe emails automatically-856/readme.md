## 简介
**Send daily recipe emails automatically**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/856

---

# Send daily recipe emails automatically


## 节点清单

| 节点 | 类型 |
|------|------|
| Cron | 定时触发器 |
| Search Criteria | 数据设置 |
| Set Query Values | Function |
| Set Recipe ID Values | Function |
| Retrieve Recipe Counts | HTTP Request |
| Retrieve Recipes | HTTP Request |
| Set Counts | 数据设置 |
| Send Recipes | Email 发送 |
| Create Email Body in HTML | Function |

## 触发方式
- Cron 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
