## 简介
**Set alert on the website changes**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/426

---

# Set alert on the website changes


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| IF | IF 判断 |
| Discord | Discord |
| Discord1 | Discord |
| Cron | 定时触发器 |



## 功能说明

监控告警系统，异常检测并发送通知。

手动触发，通过 Discord + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：手动或子流程调用

## 触发方式
- Cron 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：1
- 输出节点：3
- 分类：devops
