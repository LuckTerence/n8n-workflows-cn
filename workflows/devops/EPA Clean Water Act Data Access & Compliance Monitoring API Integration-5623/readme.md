## 简介
**EPA Clean Water Act Data Access & Compliance Monitoring API Integration**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5623

---

# EPA Clean Water Act Data Access & Compliance Monitoring API Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| U.S. EPA Enforcement and Compliance History Online (ECHO) - Clean Water Act (CWA) Rest Services MCP Server | MCP 触发器 |
| Fetch CWA Download Data | HTTP Request 工具 |
| Submit CWA Download Data | HTTP Request 工具 |
| Search CWA Facilities | HTTP Request 工具 |
| Submit CWA Facility Search | HTTP Request 工具 |
| Fetch CWA Facility Details | HTTP Request 工具 |
| Submit CWA Facility Details | HTTP Request 工具 |
| Fetch CWA GeoJSON Data | HTTP Request 工具 |
| Submit CWA GeoJSON Data | HTTP Request 工具 |
| Fetch CWA Info Clusters | HTTP Request 工具 |
| Submit CWA Info Clusters | HTTP Request 工具 |
| Fetch CWA Map Data | HTTP Request 工具 |
| Submit CWA Map Data | HTTP Request 工具 |
| Fetch CWA Paginated Results | HTTP Request 工具 |
| Submit CWA Paginated Results | HTTP Request 工具 |
| Fetch CWA Metadata | HTTP Request 工具 |
| Submit CWA Metadata | HTTP Request 工具 |
| Fetch BP Tribes Data | HTTP Request 工具 |
| Submit BP Tribes Data | HTTP Request 工具 |
| Fetch CWA Parameters | HTTP Request 工具 |
| Submit CWA Parameters | HTTP Request 工具 |
| Fetch CWA Pollutants | HTTP Request 工具 |
| Submit CWA Pollutants | HTTP Request 工具 |
| Fetch Federal Agencies | HTTP Request 工具 |
| Submit Federal Agencies | HTTP Request 工具 |
| Fetch ICIS Inspection Types | HTTP Request 工具 |
| Submit ICIS Inspection Types | HTTP Request 工具 |
| Fetch ICIS Law Sections | HTTP Request 工具 |
| Submit ICIS Law Sections | HTTP Request 工具 |
| Fetch NAICS Codes | HTTP Request 工具 |
| Submit NAICS Codes | HTTP Request 工具 |
| Fetch NPDES Parameters | HTTP Request 工具 |
| Submit NPDES Parameters | HTTP Request 工具 |
| Fetch WBD Codes | HTTP Request 工具 |
| Submit WBD Codes | HTTP Request 工具 |
| Fetch WBD Names | HTTP Request 工具 |
| Submit WBD Names | HTTP Request 工具 |



## 功能说明

监控告警系统，异常检测并发送通知。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：37
- 触发方式：手动或子流程调用

## 触发方式
- U.S. EPA Enforcement and Compliance History Online (ECHO) - Clean Water Act (CWA) Rest Services MCP Server 触发

## 统计
- 节点总数：37
- 触发节点：1
- 处理节点：0
- 输出节点：36
- 分类：devops
