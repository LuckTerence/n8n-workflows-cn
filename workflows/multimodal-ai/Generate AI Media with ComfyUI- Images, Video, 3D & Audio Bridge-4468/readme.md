## 简介
**Generate AI Media with ComfyUI: Images, Video, 3D & Audio Bridge**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4468

---

# Generate AI Media with ComfyUI: Images, Video, 3D & Audio Bridge


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Edit Fields | 数据设置 |
| HTTP Request | HTTP Request |
| If | IF 判断 |
| Wait | 等待 |
| Get Generated Image | HTTP Request |
| Fail Get History | Code |
| Connection Config | 数据设置 |
| Trigger LOCAL Workflow | HTTP Request |
| Fail Trigger | Code |
| Write to error log | 读写文件 |
| Convert to File | 转换为文件 |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Discord Alert | Discord |
| When clicking ‘Test workflow’ | 手动触发 |
| 🎨🏠 Run local ComfyUI workflow | 执行工作流 |
| Upload Attachments LOCAL | HTTP Request |
| Fail Upload | Code |
| Client ID | 加密 |
| Wait For Test Type Select | 等待 |
| If Img2Img | IF 判断 |
| Connection Config Duplicate | 数据设置 |
| Fallback Txt2Img SDXL Turbo | 数据设置 |
| Wait1 | 等待 |
| Link This To Error Handling | 空操作 |
| Fallback Img2Img SDXL Turbo | 数据设置 |
| Return The Output JSON Instead | 数据设置 |
| Read API Exported Img2Img ComfyUI Workflow from Disk | 读写文件 |
| Extract Img2Img Comfy Workflow | 从文件提取 |
| Edit Img2Img Inputs | 数据设置 |
| Read API Exported Txt2Img ComfyUI Workflow from Disk | 读写文件 |
| Extract Txt2Img Comfy Workflow | 从文件提取 |
| Edit Txt2Img Inputs | 数据设置 |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 Discord + HTTP API 实现自动化。

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

- 节点总数：34
- 触发方式：手动触发

## 触发方式
- When Executed by Another Workflow 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：34
- 触发节点：2
- 处理节点：27
- 输出节点：5
- 分类：multimodal-ai
