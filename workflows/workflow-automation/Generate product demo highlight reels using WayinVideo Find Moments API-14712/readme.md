## 简介
**Generate product demo highlight reels using WayinVideo Find Moments API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14712

---

# Generate product demo highlight reels using WayinVideo Find Moments API


## 节点清单

| 节点 | 类型 |
|------|------|
| 1. Form — Demo URL + Query + Email | 表单触发器 |
| 2. WayinVideo — Submit Find Moments | HTTP Request |
| 3. Wait — 90 Seconds | 等待 |
| 4. WayinVideo — Get Moments Result | HTTP Request |
| 5. IF — Status SUCCEEDED? | IF 判断 |
| 6. Wait — 30 Seconds Retry | 等待 |
| 7. Gmail — Send Review Email | Email 发送 |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Product)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：表单提交触发

## 触发方式
- 1. Form — Demo URL + Query + Email 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
