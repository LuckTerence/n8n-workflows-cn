## 简介
**Readable Workflow Export & Deployment Pipeline for Multi-Environment CI-CD**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3994

---

# Readable Workflow Export & Deployment Pipeline for Multi-Environment CI-CD


## 节点清单

| 节点 | 类型 |
|------|------|
| Remove root node | 数据设置 |
| TAG? Auto deploy to dev | IF 判断 |
| TAG? Auto deploy to PROD | IF 判断 |
| Start export workflows | 手动触发 |
| Create folders and run n8n cli | 执行命令 |
| load exported workflows | 读写文件 |
| parse workflow | 从文件提取 |
| Create JSON file with readable name | 转换为文件 |
| Store named workflow | 读写文件 |
| Create JSON file with readable name (dev) | 转换为文件 |
| Create JSON file with readable name (prod) | 转换为文件 |
| Store named workflow (dev) | 读写文件 |
| Store named workflow (prod) | 读写文件 |



## 功能说明

自动部署流水线，代码提交后自动构建和发布。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- Start export workflows 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：12
- 输出节点：0
- 分类：workflow-automation
