## 简介
**Audit Confluence space permissions and public links for compliance**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12239

---

# Audit Confluence space permissions and public links for compliance


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Variables | 数据设置 |
| Confluence - GQL Space Anonymous Access | graphql |
| Split Out Spaces | 数据拆分 |
| Confluence - GQL Space Public Links Enabled | graphql |
| Confluence - GQL Space Pages with Public Link | graphql |
| Merge | 数据合并 |
| Set Anonymous Access | 数据设置 |
| Set Space Public Links Enabled | 数据设置 |
| Set Space Pages with Public Link | 数据设置 |
| Confluence - Get Spaces | HTTP Request |
| Build Report | 数据设置 |



## 功能说明

Audit Confluence space permissions and public link。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
