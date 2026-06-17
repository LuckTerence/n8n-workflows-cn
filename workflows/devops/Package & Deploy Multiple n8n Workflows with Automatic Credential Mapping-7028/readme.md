## 简介
**Package & Deploy Multiple n8n Workflows with Automatic Credential Mapping**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7028

---

# Package & Deploy Multiple n8n Workflows with Automatic Credential Mapping


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Installer Data | 数据设置 |
| Convert to File | 转换为文件 |
| Extract Workflow | 数据设置 |
| Create Workflow | n8n |
| Loop Over Workflows | 分批处理 |
| Decompress Workflows | 从文件提取 |
| Split Workflows | 数据拆分 |
| If 3 Credentials | IF 判断 |
| Stop and Error | 停止并报错 |
| Github Credentials | github |
| OpenAi Credentials | HTTP Request |
| n8n Credentials | n8n |
| Credential Dictionary | 数据设置 |
| Fix Credentials | Code |
| Move to Project | HTTP Request |
| Extract Project Details | 数据设置 |
| Merge | 数据合并 |
| No Op | 空操作 |
| Install Success1 | 空操作 |
| Done | 空操作 |
| If Project | IF 判断 |



## 功能说明

自动部署流水线，代码提交后自动构建和发布。

手动触发，通过 Git + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：19
- 输出节点：2
- 分类：devops
