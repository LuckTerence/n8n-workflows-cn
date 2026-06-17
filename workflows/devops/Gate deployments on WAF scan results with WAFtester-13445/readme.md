## 简介
**Gate deployments on WAF scan results with WAFtester**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13445

---

# Gate deployments on WAF scan results with WAFtester


## 节点清单

| 节点 | 类型 |
|------|------|
| Deploy Webhook | Webhook |
| Detect WAF | HTTP Request |
| Start Scan | HTTP Request |
| Wait for Scan | 等待 |
| Poll Task Status | HTTP Request |
| Parse Results | Code |
| Pass or Fail? | IF 判断 |
| Respond Pass | 响应 Webhook |
| Respond Fail | 响应 Webhook |



## 功能说明

自动部署流水线，代码提交后自动构建和发布，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- Deploy Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：3
- 输出节点：5
- 分类：devops
