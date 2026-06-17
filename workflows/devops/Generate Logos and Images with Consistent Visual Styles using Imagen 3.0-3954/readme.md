## 简介
**Generate Logos and Images with Consistent Visual Styles using Imagen 3.0**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3954

---

# Generate Logos and Images with Consistent Visual Styles using Imagen 3.0


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Out | 数据拆分 |
| Imagen 3.0 | HTTP Request |
| Variables | 数据设置 |
| Download Image | HTTP Request |
| On form submission | 表单触发器 |
| Form Validation | IF 判断 |
| Retry Form | 表单 |
| Upload to Cloudinary | HTTP Request |
| Convert to File1 | 转换为文件 |
| Generate HTML | HTML |
| Convert to File | 转换为文件 |
| Form Ending | 表单 |
| Has Email? | IF 判断 |
| Send Results to Email | Email 发送 |
| Image to Base64 | 从文件提取 |
| Gemini 2.0 | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图（Logos)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：10
- 输出节点：5
- 分类：devops
