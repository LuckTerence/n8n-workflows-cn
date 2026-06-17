## 简介
**Parse DMARC reports, save them in database and notify on DKIM or SPF error**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2369

---

# Parse DMARC reports, save them in database and notify on DKIM or SPF error


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| End date format | 日期时间 |
| If multiple records to parse | IF 判断 |
| Map fields for DB input and parse | 数据设置 |
| Begin format date | 日期时间 |
| Input into database | MySQL |
| If issue with DKIM or SPF | IF 判断 |
| Rename Keys | renameKeys |
| Rename column for consistency | 数据设置 |
| Unzip File | compression |
| Extract XML data | 从文件提取 |
| Parse XML data to JSON | XML |
| Split Out For Separate Entries | 数据拆分 |
| Slack Post Message On Channel | Slack |
| Send Error Notification Email | Email 发送 |

## 触发方式
- 手动触发

## 统计
- 节点总数：15
- 触发节点：0
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
