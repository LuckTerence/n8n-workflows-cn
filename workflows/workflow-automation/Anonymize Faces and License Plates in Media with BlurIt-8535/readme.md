## 简介
**Anonymize Faces and License Plates in Media with BlurIt**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8535

---

# Anonymize Faces and License Plates in Media with BlurIt


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Auth Config | 数据设置 |
| Auth Get Token | HTTP Request |
| Upload Input File | 表单触发器 |
| Create Blurit Task | HTTP Request |
| Merge | 数据合并 |
| Wait | 等待 |
| Get Task Status | HTTP Request |
| Switch | Switch 路由 |
| Get Result File | HTTP Request |



## 功能说明

Anonymize Faces and License Plates in Media with B（自动化)表单提交触发，通过 HTTP API 实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- Upload Input File 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
