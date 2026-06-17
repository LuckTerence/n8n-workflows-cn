## 简介
**Extract And Decode Google News RSS URLs to Clean Article Links**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3150

---

# Extract And Decode Google News RSS URLs to Clean Article Links


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Limit | 数据限制 |
| Reading Google News RSS | RSS Feed |
| Decoded url | 数据设置 |
| Call decoding URL | HTTP Request |
| Prepare decoding variables | Code |
| Get encoded news URL | HTTP Request |
| Map needed keys | 数据设置 |
| Extract decoding keys | HTML |
| Aggregate results in a single object | 数据聚合 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Reading Google News RSS 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
