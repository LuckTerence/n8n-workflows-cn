## 简介
**College Football Analytics Platform with Comprehensive Data API Access**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5493

---

# College Football Analytics Platform with Comprehensive Data API Access


## 节点清单

| 节点 | 类型 |
|------|------|
| College Football Data MCP Server | MCP 触发器 |
| Season calendar | HTTP Request 工具 |
| Advanced box scores | HTTP Request 工具 |
| Games and results | HTTP Request 工具 |
| Game media information and schedules | HTTP Request 工具 |
| Player game stats | HTTP Request 工具 |
| Team game stats | HTTP Request 工具 |
| Game weather information (Patreon only) | HTTP Request 工具 |
| Team records | HTTP Request 工具 |
| Live game results (Patreon only) | HTTP Request 工具 |
| Coaching records and history | HTTP Request 工具 |
| Conferences | HTTP Request 工具 |
| List of NFL Draft picks | HTTP Request 工具 |
| List of NFL positions | HTTP Request 工具 |
| List of NFL teams | HTTP Request 工具 |
| Drive data and results | HTTP Request 工具 |
| Betting lines | HTTP Request 工具 |
| Live metrics and PBP (Patreon only) | HTTP Request 工具 |
| Types of player play stats | HTTP Request 工具 |
| Play stats by play | HTTP Request 工具 |
| Play types | HTTP Request 工具 |
| Play by play data | HTTP Request 工具 |
| Win probability chart data | HTTP Request 工具 |
| Pregame win probability data | HTTP Request 工具 |
| Team Predicated Points Added (PPA/EPA) by game | HTTP Request 工具 |
| Player Predicated Points Added (PPA/EPA) broken do | HTTP Request 工具 |
| Player Predicated Points Added (PPA/EPA) broken do 1 | HTTP Request 工具 |
| Predicted Points (i.e. Expected Points or EP) | HTTP Request 工具 |
| Predicted Points Added (PPA/EPA) data by team | HTTP Request 工具 |
| Transfer portal by season | HTTP Request 工具 |
| Team returning production metrics | HTTP Request 工具 |
| Search for player information | HTTP Request 工具 |
| Player usage metrics broken down by season | HTTP Request 工具 |
| Player stats by season | HTTP Request 工具 |
| Historical polls and rankings | HTTP Request 工具 |
| Historical Elo ratings | HTTP Request 工具 |
| Historical SP+ ratings | HTTP Request 工具 |
| Historical SP+ ratings by conference | HTTP Request 工具 |
| Historical SRS ratings | HTTP Request 工具 |
| Recruit position group ratings | HTTP Request 工具 |
| Player recruiting ratings and rankings | HTTP Request 工具 |
| Team recruiting rankings and ratings | HTTP Request 工具 |
| Team rosters | HTTP Request 工具 |
| Team talent composite rankings | HTTP Request 工具 |
| Team information | HTTP Request 工具 |
| FBS team list | HTTP Request 工具 |
| Team matchup history | HTTP Request 工具 |
| Team stat categories | HTTP Request 工具 |
| Advanced team metrics by game | HTTP Request 工具 |
| Team statistics by season | HTTP Request 工具 |
| Advanced team metrics by season | HTTP Request 工具 |
| Arena and venue information | HTTP Request 工具 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

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

- 节点总数：52
- 触发方式：手动或子流程调用

## 触发方式
- College Football Data MCP Server 触发

## 统计
- 节点总数：52
- 触发节点：1
- 处理节点：0
- 输出节点：51
- 分类：workflow-automation
