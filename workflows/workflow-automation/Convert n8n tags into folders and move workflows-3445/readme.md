# Convert n8n tags into folders and move workflows

https://n8nworkflows.xyz/workflows/3445

## 节点清单

| 节点 | 类型 |
|------|------|
| set credentials | 数据设置 |
| login n8n | HTTP Request |
| get tags | HTTP Request |
| my-projects | HTTP Request |
| Split Out | 数据拆分 |
| filter owned projects | 过滤器 |
| Get folders | HTTP Request |
| Split Out2 | 数据拆分 |
| Remove Duplicates | 去重 |
| Loop Over Items | 分批处理 |
| get workflows | n8n |
| Move workflow to folder | HTTP Request |
| Normalize names | 数据设置 |
| Limit1 | 数据限制 |
| Create folders | HTTP Request |
| set folder name + id | 数据设置 |
| set folder name + id1 | 数据设置 |
| set global | 数据设置 |
| Filter | 过滤器 |
| Edit Fields | 数据设置 |
| On form submission | 表单触发器 |
| Code | Code |
| If no folder | IF 判断 |
| If folder exists | IF 判断 |
| set name | 数据设置 |
| end import | 表单 |
| pass all items | 数据设置 |
| select tags to move | 表单 |
| extract name from form | 数据设置 |
| Split Out the tags | 数据拆分 |
| tags to string | 数据设置 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：24
- 输出节点：6
- 分类：workflow-automation
