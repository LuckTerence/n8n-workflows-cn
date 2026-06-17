## 简介
**Batch Convert CAD-BIM Files to XLSX-DAE with Validation and Reporting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7650

---

# Batch Convert CAD-BIM Files to XLSX-DAE with Validation and Reporting


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Capture Pipeline Start Time1 | Code |
| Merge Pipeline Start with Config1 | 数据合并 |
| Set Configuration Parameters1 | 数据设置 |
| Find CAD Files1 | 执行命令 |
| Merge Config with Search Results1 | 数据合并 |
| Process File List1 | Code |
| Check if Files Exist1 | IF 判断 |
| Split Files for Processing1 | 数据拆分 |
| Create Output Directory1 | 执行命令 |
| Merge File Data1 | 数据合并 |
| Capture Start Time1 | Code |
| Small Delay | 等待 |
| Execute Conversion1 | 执行命令 |
| Calculate Conversion Time1 | Code |
| Merge Data Before Verification1 | 数据合并 |
| Verify Output Files and Get Sizes1 | 执行命令 |
| Complete File Verification1 | Code |
| Generate HTML Report1 | Code |
| Prepare Binary Data1 | Code |
| Save HTML File1 | 写入二进制文件 |
| Verify and Prepare Path1 | Code |
| Open HTML Report1 | 执行命令 |
| Final Completion Notice1 | 执行命令 |
| No Files Found Response1 | 数据设置 |
| Schedule Trigger1 | 定时触发器 |



## 功能说明

文件处理工具，自动转换或管理文件，定时执行。

定时触发、手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：手动触发, 定时触发

## 触发方式
- Manual Trigger 触发
- Schedule Trigger1 触发

## 统计
- 节点总数：26
- 触发节点：2
- 处理节点：24
- 输出节点：0
- 分类：workflow-automation
