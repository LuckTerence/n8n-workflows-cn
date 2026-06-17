## 简介
**Automatically Correct Wrong Shipping Addresses in Billbee Orders**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：20 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2609

---

# Automatically Correct Wrong Shipping Addresses in Billbee Orders


## 节点清单

| 节点 | 类型 |
|------|------|
| get order data | HTTP Request |
| Split Out Order Data | 数据拆分 |
| Set Address Fields | 数据设置 |
| Check Address endereco api | HTTP Request |
| Split Out Corrected Address | 数据拆分 |
| set new delivery address to billbee | HTTP Request |
| Wait | 等待 |
| Wait1 | 等待 |
| check if new address is not empty | IF 判断 |
| set billbee tag | HTTP Request |
| check if housenumer is not empty | IF 判断 |
| check if addressline 2 contains number | IF 判断 |
| Filter | 过滤器 |
| set value of addressline2 as housenumber | 数据设置 |
| Filter Out PickUpShops | 过滤器 |
| check if addressline 2 contains number and letter | IF 判断 |
| set billbee tag manual check | HTTP Request |
| set value of addressline2 as housenumber number+letter | 数据设置 |
| set billbee success | HTTP Request |
| ConfigNode | 数据设置 |
| Webhook | Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：workflow-automation
