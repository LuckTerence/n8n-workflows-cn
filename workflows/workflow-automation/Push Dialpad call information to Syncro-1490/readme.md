# Push Dialpad call information to Syncro

https://n8nworkflows.xyz/workflows/1490

## 节点清单

| 节点 | 类型 |
|------|------|
| GetCustomer | HTTP Request |
| Webhook | Webhook |
| CreateTicket | HTTP Request |
| GetTicket | HTTP Request |
| IFMoreThanOne | IF 判断 |
| Google Sheets | Google Sheets |
| ForGoogle | 数据设置 |
| UpdateTicket | HTTP Request |
| ForGoogle1 | 数据设置 |
| Google Sheets1 | Google Sheets |
| NoOp | 空操作 |
| Contacts | Function |
| IFContacts | IF 判断 |
| Customers | Function |
| IFCustomers | IF 判断 |
| NoOp1 | 空操作 |
| CreateTicketForCustomer | HTTP Request |
| ForGoogle2 | 数据设置 |
| Google Sheets2 | Google Sheets |
| EnvVariables | 数据设置 |
| IF | IF 判断 |
| NoOp2 | 空操作 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
