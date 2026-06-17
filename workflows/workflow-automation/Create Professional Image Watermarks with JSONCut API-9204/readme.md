## 简介
**Create Professional Image Watermarks with JSONCut API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9204

---

# Create Professional Image Watermarks with JSONCut API


## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger | 表单触发器 |
| Upload Main Image | HTTP Request |
| Upload Watermark | HTTP Request |
| Merge Uploads | 数据合并 |
| Wait | 等待 |
| If Success | IF 判断 |
| If Error | IF 判断 |
| Download Image | HTTP Request |
| Error Stop | 停止并报错 |
| Aggregate | 数据聚合 |
| Create JsonCut Job | HTTP Request |
| Check JsonCut job Status | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图（Professional)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：表单提交触发

## 触发方式
- Form Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
