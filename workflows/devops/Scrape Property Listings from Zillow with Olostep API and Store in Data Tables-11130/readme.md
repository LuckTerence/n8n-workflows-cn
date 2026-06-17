## 简介
**Scrape Property Listings from Zillow with Olostep API and Store in Data Tables**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11130

---

# Scrape Property Listings from Zillow with Olostep API and Store in Data Tables


## 节点清单

| 节点 | 类型 |
|------|------|
| parsedInfo | 数据设置 |
| Split Out | 数据拆分 |
| scrape places | HTTP Request |
| Insert row | 数据表 |
| Loop Over Items | 分批处理 |
| Edit Fields | 数据设置 |
| Split Out1 | 数据拆分 |
| On form submission | 表单触发器 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：devops
