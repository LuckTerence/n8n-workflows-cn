## 简介
**Send sales data from Webhook to Mautic**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/467

---

# Send sales data from Webhook to Mautic


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Mautic | mautic |
| Find User | mautic |
| Update User | mautic |
| Tag User | mautic |
| Unsubscribe User | mautic |
| Split Full Name | Function |
| If not found return -1 | Function |
| @MAIN STUDENT DATA | 数据合并 |
| Remove unsubscribe | mautic |
| Find User To Tag Sale | mautic |
| Set userFound | 数据设置 |
| Switch Webhook Types | Switch 路由 |
| Set Webhook Request | 数据设置 |
| IF NOT userFound | IF 判断 |
| Switch User.type | Switch 路由 |
| IF unsubscribe_from_marketing_emails | IF 判断 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：16
- 输出节点：0
- 分类：workflow-automation
