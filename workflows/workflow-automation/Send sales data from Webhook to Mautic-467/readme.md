# Send sales data from Webhook to Mautic

https://n8nworkflows.xyz/workflows/467

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
