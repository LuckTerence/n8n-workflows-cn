## 简介
**Classify & Extract Data from Floorplans with Mistral AI OCR & JigsawStack**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8420

---

# Classify & Extract Data from Floorplans with Mistral AI OCR & JigsawStack


## 节点清单

| 节点 | 类型 |
|------|------|
| Check – GDPR Consent | IF 判断 |
| Webhook – Receive Upload | Webhook |
| Respond – Consent Required | 响应 Webhook |
| Process – Multiple File Uploads | Code |
| Check – File Type (PDF/Image) | IF 判断 |
| Extract – PDF Metadata/Text | 从文件提取 |
| Check – File Size & Pages | IF 判断 |
| Analyze – Confidence Score (Heuristics) | Code |
| Route – Confidence Levels | Switch 路由 |
| Respond – Low Quality/Drop | 响应 Webhook |
| Classify – Image Files | HTTP Request |
| Classify – PDF Text | HTTP Request |
| Respond – Classification Result (Image) | 响应 Webhook |
| Respond – Classification Result (PDF) | 响应 Webhook |
| Respond – File Too Large | 响应 Webhook |
| Upload – JigsawStack (Storage) | HTTP Request |
| No Operation, do nothing | 空操作 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：Webhook 触发

## 触发方式
- Webhook – Receive Upload 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
