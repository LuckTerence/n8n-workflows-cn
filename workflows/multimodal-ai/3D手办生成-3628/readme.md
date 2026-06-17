## 简介
**3D手办生成**

Midjourney+GPT-4o生成3D模型多视角图

> 分类：多模态 AI | 适配等级：A（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3628

---

# 3D手办生成


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Midjourney Generator | HTTP Request |
| Get Midjourney URL | HTTP Request |
| Verify URL Acquisition | IF 判断 |
| Wait for Generation | 等待 |
| Get Random Image URL | Code |
| Generation 3-view Image with GPT-4o-Image | HTTP Request |
| Check if the URL is obtained | IF 判断 |
| Get Final Output | Code |
| Get Image | Code |



## 功能说明

3D手办生成。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：multimodal-ai
