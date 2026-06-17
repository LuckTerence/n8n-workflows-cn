## 简介
**Access Complete Vehicle Data with Marketcheck APIs for AI Agents**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5527

---

# Access Complete Vehicle Data with Marketcheck APIs for AI Agents


## 节点清单

| 节点 | 类型 |
|------|------|
| Marketcheck APIs MCP Server | MCP 触发器 |
| Get dealers active inventory | HTTP Request 工具 |
| Listing by id | HTTP Request 工具 |
| Long text Listings attributes for Listing with the | HTTP Request 工具 |
| Listing media by id | HTTP Request 工具 |
| Listing by id 1 | HTTP Request 工具 |
| Long text Listings attributes for Listing with the 1 | HTTP Request 工具 |
| Listing media by id 1 | HTTP Request 工具 |
| Listing by id 2 | HTTP Request 工具 |
| Long text Listings attributes for Listing with the 2 | HTTP Request 工具 |
| Listing media by id 2 | HTTP Request 工具 |
| Listing by id 3 | HTTP Request 工具 |
| Long text Listings attributes for Listing with the 3 | HTTP Request 工具 |
| Listing media by id 3 | HTTP Request 工具 |
| Gets active car listings for the given search crit | HTTP Request 工具 |
| Gets active auction car listings for the given sea | HTTP Request 工具 |
| API for auto-completion of inputs | HTTP Request 工具 |
| Gets active private party car listings for the giv | HTTP Request 工具 |
| Gets Recent car listings for the given search crit | HTTP Request 工具 |
| Gets active car listings in UK for the given searc | HTTP Request 工具 |
| Gets Recent UK car listings for the given search c | HTTP Request 工具 |
| Recall info by vin | HTTP Request 工具 |
| get client filters | HTTP Request 工具 |
| set client filters | HTTP Request 工具 |
| CRM check of a particular vin | HTTP Request 工具 |
| Dealer by id | HTTP Request 工具 |
| Dealer by id 1 | HTTP Request 工具 |
| Dealer by id 2 | HTTP Request 工具 |
| Dealer by id 3 | HTTP Request 工具 |
| Dealer by id 4 | HTTP Request 工具 |
| Find car dealers around | HTTP Request 工具 |
| Find car dealers around 1 | HTTP Request 工具 |
| Find car dealers around 2 | HTTP Request 工具 |
| Find car dealers around 3 | HTTP Request 工具 |
| Find car dealers around 4 | HTTP Request 工具 |
| EPI VIN Decoder | HTTP Request 工具 |
| NeoVIN Decoder | HTTP Request 工具 |
| VIN Decoder | HTTP Request 工具 |
| API for auto-completion of inputs based on taxonom | HTTP Request 工具 |
| API for getting terms from taxonomy | HTTP Request 工具 |
| Get a cars online listing history | HTTP Request 工具 |
| Get a cars online listing history 1 | HTTP Request 工具 |
| Fetch cached image | HTTP Request 工具 |
| Heavy equipment listing by id | HTTP Request 工具 |
| Long text Heavy equipment Listings attributes for | HTTP Request 工具 |
| Listing media by id 4 | HTTP Request 工具 |
| Gets active heavy equipment listings for the given | HTTP Request 工具 |
| API for auto-completion of inputs 1 | HTTP Request 工具 |
| Motorcycle listing by id | HTTP Request 工具 |
| Long text Motorcycle Listings attributes for Listi | HTTP Request 工具 |
| Motorcycle listing media by id | HTTP Request 工具 |
| Gets active motorcycle listings for the given sear | HTTP Request 工具 |
| API for auto-completion of inputs 2 | HTTP Request 工具 |
| RV listing by id | HTTP Request 工具 |
| Long text RV Listings attributes for Listing with | HTTP Request 工具 |
| Listing media by id 5 | HTTP Request 工具 |
| RV listing by id 1 | HTTP Request 工具 |
| Long text RV Listings attributes for Listing with 1 | HTTP Request 工具 |
| Listing media by id 6 | HTTP Request 工具 |
| Gets active RV listings for the given search crite | HTTP Request 工具 |
| API for auto-completion of inputs 3 | HTTP Request 工具 |
| Gets active RV listings for the given search crite 1 | HTTP Request 工具 |
| Market Days Supply | HTTP Request 工具 |
| Get make model wise top 50 popular cars on nationa | HTTP Request 工具 |
| Predict car price based on it's specifications | HTTP Request 工具 |
| Predict fare value of car for UK based on YMMT & m | HTTP Request 工具 |
| Predict car price for UK based on it's specificati | HTTP Request 工具 |
| Get sales count by make, model, year, trim or taxo | HTTP Request 工具 |
| Price, Miles and Days on Market stats | HTTP Request 工具 |
| Compute relative rank for car listings. | HTTP Request 工具 |
| Compute relative rank for car listings. 1 | HTTP Request 工具 |
| Gets oem incentive listings for the given search c | HTTP Request 工具 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：72
- 触发方式：手动或子流程调用

## 触发方式
- Marketcheck APIs MCP Server 触发

## 统计
- 节点总数：72
- 触发节点：1
- 处理节点：0
- 输出节点：71
- 分类：ai-agent
