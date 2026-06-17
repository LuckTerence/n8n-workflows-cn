## 简介
**Auto-clip long videos into viral short clips with Vizard AI and social publishing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12054

---

# Auto-clip long videos into viral short clips with Vizard AI and social publishing


## 节点清单

| 节点 | 类型 |
|------|------|
| Configuration | 数据设置 |
| Get Status | HTTP Request |
| Wait | 等待 |
| Check Status | Switch 路由 |
| Split Clips | 数据拆分 |
| On form submission | 表单触发器 |
| Filter by Viral Score | 过滤器 |
| Append Source (Success) | Google Sheets |
| Append Source (Failed) 2 | Google Sheets |
| Append Source (Failed) | Google Sheets |
| AI Clipper | HTTP Request |
| Success? | IF 判断 |
| Post to Tiktok | HTTP Request |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Auto)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
