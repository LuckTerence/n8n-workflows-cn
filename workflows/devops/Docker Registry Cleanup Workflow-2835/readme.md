## 简介
**Docker Registry Cleanup Workflow**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2835

---

# Docker Registry Cleanup Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Manifest Digest | HTTP Request |
| Remove Old Tags | HTTP Request |
| Retrieve Image Tags | HTTP Request |
| List Images | HTTP Request |
| Extract Image Names | Code |
| Identify Tags to Remove | Code |
| Scheduled Trigger | 定时触发器 |
| Send Notification Email | Email 发送 |
| Split Tags | 数据拆分 |
| Filter Valid Tags | 过滤器 |
| Fetch Manifest Digest for Blob | HTTP Request |
| Update Fields | 数据设置 |
| Group Tags by Image | Code |
| Sort by Creation Date | 数据排序 |
| Send Failure Notification Email | Email 发送 |
| Execute Garbage Collection | SSH |



## 功能说明

自动部署流水线，代码提交后自动构建和发布，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Scheduled Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：8
- 输出节点：7
- 分类：devops
