## 简介
**Convert GIF to MP4 with FFmpegAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8321

---

# Convert GIF to MP4 with FFmpegAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Upload URL | HTTP Request |
| Upload File | HTTP Request |
| Merge | 数据合并 |
| Process File | HTTP Request |
| Attach file | 表单触发器 |
| Download URL | 表单 |



## 功能说明

文件处理工具，自动转换或管理文件（Gif)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：6
- 触发方式：表单提交触发

## 触发方式
- Attach file 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
