## 简介
**E-commerce bestseller video generator (Algolia + Google VEO 3)**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11119

---

# E-commerce bestseller video generator (Algolia + Google VEO 3)


## 节点清单

| 节点 | 类型 |
|------|------|
| Every week on monday morning | 定时触发器 |
| Test Trigger while building the workflow | 手动触发 |
| Get weekly bestseller from Algolia | HTTP Request |
| If no video for that product | IF 判断 |
| Image URL is present | IF 判断 |
| Check image availability | HTTP Request |
| No Operation, do nothing | 空操作 |
| Tell admin that bestseller has no image | Email 发送 |
| Tell admin that bestseller has broken image | Email 发送 |
| Image is present and valid | IF 判断 |
| Wait for video generation | 等待 |
| Finished ? | IF 判断 |
| Wait more | 等待 |
| Generate video with Google VEO 3 | HTTP Request |
| Get video name and storage bucket | 数据设置 |
| Checking if we're done | HTTP Request |
| Downloading the MP4 file | HTTP Request |
| Drop video in Supabase Bucket | HTTP Request |
| Aggregate | 数据聚合 |
| Index in Algolia | HTTP Request |
| Convert image to base64 for VEO 3 | 从文件提取 |



## 功能说明

AI 视频生成工作流，自动创作视频内容，定时执行。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：定时触发, 手动触发

## 触发方式
- Every week on monday morning 触发
- Test Trigger while building the workflow 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：10
- 输出节点：9
- 分类：multimodal-ai
