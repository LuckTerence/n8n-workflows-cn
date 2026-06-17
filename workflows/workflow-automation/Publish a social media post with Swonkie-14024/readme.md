## 简介
**Publish a social media post with Swonkie**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14024

---

# Publish a social media post with Swonkie


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Configure | 数据设置 |
| Create Media Entry | HTTP Request |
| Download & Attach Binary | HTTP Request |
| Upload File to Blob | HTTP Request |
| Confirm Upload | HTTP Request |
| Wait for Processing | 等待 |
| Check Media Status | HTTP Request |
| Media Ready? | Switch 路由 |
| Create Post | HTTP Request |
| Validate Post | HTTP Request |
| Post Valid? | IF 判断 |
| Change Stage | HTTP Request |
| Post Published | 数据设置 |
| Media Processing Failed | 停止并报错 |
| Validation Failed | 停止并报错 |



## 功能说明

社交媒体管理，多平台内容发布和监听。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：16
- 触发方式：手动触发

## 触发方式
- Start 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：7
- 输出节点：8
- 分类：workflow-automation
