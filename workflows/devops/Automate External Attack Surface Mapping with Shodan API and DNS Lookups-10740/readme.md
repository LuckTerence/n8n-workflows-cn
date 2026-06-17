## 简介
**Automate External Attack Surface Mapping with Shodan API and DNS Lookups**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10740

---

# Automate External Attack Surface Mapping with Shodan API and DNS Lookups


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Test workflow' | 手动触发 |
| Set Target Domain1 | 数据设置 |
| DNS Lookup (Google)1 | HTTP Request |
| Extract DNS Records1 | Code |
| Filter: Only IP records1 | IF 判断 |
| Prepare IP Item1 | 数据设置 |
| Delay (rate-limit) | 等待 |
| Shodan Search by IP | HTTP Request |
| Parse Shodan Data | Code |
| Log to Google Sheets1 | Google Sheets |
| Notify: Results (console log) | 数据设置 |
| Error Handler (catch) | 空操作 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：9
- 输出节点：2
- 分类：devops
