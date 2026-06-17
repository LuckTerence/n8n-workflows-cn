## 简介
**Phishing Analysis - URLScan.io and VirusTotal**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1992

---

# Phishing Analysis - URLScan.io and VirusTotal


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| sends slack message | Slack |
| Split In Batches | 分批处理 |
| Mark as read | Outlook |
| VirusTotal: Scan URL | HTTP Request |
| VirusTotal: Get report | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Find indicators of compromise | Code |
| URLScan: Get report | urlScanIo |
| URLScan: Scan URL | urlScanIo |
| Has URL? | IF 判断 |
| No error? | IF 判断 |
| Not empty? | 过滤器 |
| Wait 1 Minute | 等待 |
| Get all unread messages | Outlook |
| Merge Reports | 数据合并 |



## 功能说明

Phishing Analysis - URLScan.io and VirusTotal。

定时触发、手动触发，通过 Slack + HTTP API 实现自动化。

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
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking "Execute Workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：9
- 输出节点：5
- 分类：workflow-automation
