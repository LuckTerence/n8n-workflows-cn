## 简介
**Report spam and phishing URLs from IMAP mailboxes to Spamhaus**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12846

---

# Report spam and phishing URLs from IMAP mailboxes to Spamhaus


## 节点清单

| 节点 | 类型 |
|------|------|
| Phishing Trigger | Email 读取 |
| Spam Trigger | Email 读取 |
| initial config spam | 数据设置 |
| extract all URLs | Code |
| create item for spamhaus | 数据设置 |
| Spamhaus submit url | HTTP Request |
| Loop over each email | 分批处理 |
| initial phish config | 数据设置 |
| aggregate all into a single list | 数据聚合 |
| add run specific job | 空操作 |
| add email specific job | 空操作 |
| de-duplicate URLs | 去重 |
| split URLs to array | 数据拆分 |
| filter out URLs that match regexes | 过滤器 |

## 触发方式
- 手动触发

## 统计
- 节点总数：14
- 触发节点：0
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
