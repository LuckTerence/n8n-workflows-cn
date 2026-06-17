## 简介
**Generate Secure Social Media Connection Links for Clients with Upload-Post**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8596

---

# Generate Secure Social Media Connection Links for Clients with Upload-Post


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Create user | uploadPost |
| Generate jwt for platform integration | uploadPost |
| Send a text message | Telegram |
| On form submission | 表单触发器 |
| Upload a video | uploadPost |



## 功能说明

社交媒体管理，多平台内容发布和监听。

手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：6
- 触发方式：手动触发, 表单提交触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- On form submission 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
