## 简介
**Generate Videos from Text or Images with Sora 2 AI - No Watermark**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9810

---

# Generate Videos from Text or Images with Sora 2 AI - No Watermark


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Check: Has Image? | Switch 路由 |
| Upload to ImgBB | HTTP Request |
| Download Video (Text) | HTTP Request |
| Download Video (Image) | HTTP Request |
| Check Status (Text) | HTTP Request |
| Wait (Text) | 等待 |
| Is Ready? (Text) | IF 判断 |
| TEXT TO VIDEO | HTTP Request |
| Check Status (Image) | HTTP Request |
| Wait (Image) | 等待 |
| Is Ready? (Image) | IF 判断 |
| IMAGE TO VIDEO | HTTP Request |
| Send Text to Video | Telegram |
| Send Image to Video | Telegram |



## 功能说明

AI 图像生成工作流，文生图或图生图（Videos)表单提交触发，通过 Telegram + HTTP API 实现自动化。

，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：15
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：5
- 输出节点：9
- 分类：workflow-automation
