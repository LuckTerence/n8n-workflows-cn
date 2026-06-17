## 简介
**Create Character-Consistent Images with FLUX Kontext & Post to Social via Upload Post**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4798

---

# Create Character-Consistent Images with FLUX Kontext & Post to Social via Upload Post


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Is Ready? | IF 判断 |
| Check FLUX status | HTTP Request |
| When Executed by Another Workflow | 执行工作流触发器 |
| FLUX Kontext | HTTP Request |
| Merge | 数据合并 |
| Wait 2 sec | 等待 |
| Get File from GitHub | github |
| Download Initial Image | HTTP Request |
| If | IF 判断 |
| Number of Steps | 数据设置 |
| All Prompts | 数据设置 |
| Run FLUX | 执行工作流 |
| Current Step | 数据设置 |
| Merge3 | 数据合并 |
| Upload Post | uploadPost |
| Image to Base64 | 从文件提取 |
| Get Image | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 Git + HTTP API 实现自动化。

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

- 节点总数：18
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：12
- 输出节点：4
- 分类：multimodal-ai
