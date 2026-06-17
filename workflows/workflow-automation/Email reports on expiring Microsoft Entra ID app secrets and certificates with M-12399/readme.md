## 简介
**Email reports on expiring Microsoft Entra ID app secrets and certificates with Microsoft Graph**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：15 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/12399

---

# Email reports on expiring Microsoft Entra ID app secrets and certificates with Microsoft Graph


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out Applications | 数据拆分 |
| Set Variables | 数据设置 |
| Merge | 数据合并 |
| Filter Client Secrets | 过滤器 |
| Split Out Client Secrets | 数据拆分 |
| Split Out Certificates | 数据拆分 |
| Filter Client Certificates | 过滤器 |
| Build Client Secrets Report | 数据设置 |
| Build Certificates Report | 数据设置 |
| Get EntraID Applications and Secrets | HTTP Request |
| Aggregate | 数据聚合 |
| If Expiring Secrets not empty | IF 判断 |
| No Operation, do nothing | 空操作 |
| HTML Table with Expiring Secrets | HTML |
| Send email | Email 发送 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
