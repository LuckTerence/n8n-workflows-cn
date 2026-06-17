## 简介
**Phishing Analysis - URLScan.io and VirusTotal**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
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

## 触发方式
- When clicking "Execute Workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：9
- 输出节点：5
- 分类：workflow-automation
