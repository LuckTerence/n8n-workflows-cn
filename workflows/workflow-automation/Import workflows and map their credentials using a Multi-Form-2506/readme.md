## 简介
**Import workflows and map their credentials using a Multi-Form**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2506

---

# Import workflows and map their credentials using a Multi-Form


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| Export Credentials | 执行命令 |
| Get Credentials Data | 读写文件 |
| Binary to JSON | 从文件提取 |
| Merge | 数据合并 |
| Collect Credentials to Replace | 数据合并 |
| Settings | 数据设置 |
| Prepare Request Data | Code |
| Get Workflows | HTTP Request |
| No Operation | 空操作 |
| Determine Workflow Source | IF 判断 |
| Error1 | 表单 |
| Error | 表单 |
| Split Out Workflows | 数据拆分 |
| Get Workflow Names | Code |
| Sort by updatedAt DESC | 数据排序 |
| No Operation1 | 空操作 |
| Rename Keys | renameKeys |
| Create Workflow | n8n |
| Upload File | 表单 |
| Choose Workflow | 表单 |
| Success | 表单 |
| Choose Instance | 表单 |
| On form submission | 表单触发器 |
| Generate Instance Options | Code |
| Get Selected Workflow | Code |
| Split Out Nodes | 数据拆分 |
| Filter Out Nodes Having Credentials | 过滤器 |
| Extract Credentials | 数据设置 |
| Remove Duplicate Credentials by Name | 去重 |
| Map Credentials | 表单 |
| Get Selected Credentials | Code |
| Add Old Names | 数据设置 |
| Replace Credentials in Workflow | Code |
| Generate Credential Options | Code |
| Create Empty Credentials | n8n |
| Get Missing Credentials | Code |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Workflows)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：37
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：37
- 触发节点：1
- 处理节点：35
- 输出节点：1
- 分类：workflow-automation
