## 简介
**Generate Viral Bigfoot Vlog Videos with Veo 3**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Slack/Stripe/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5312

---

# Generate Viral Bigfoot Vlog Videos with Veo 3


## 节点清单

| 节点 | 类型 |
|------|------|
| form_trigger | 表单触发器 |
| claude-4-sonnet | OpenAI Chat Model |
| split_scenes | 数据拆分 |
| scene_director | LLM Chain |
| send_and_wait | Slack |
| aggregate_scenes | 数据聚合 |
| set_scene_prompts | 数据设置 |
| reset_scene_prompts | 数据设置 |
| split_scene_prompts | 数据拆分 |
| queue_create_video | HTTP Request |
| wait | 等待 |
| fetch_status | HTTP Request |
| check_status | IF 判断 |
| fetch_result | HTTP Request |
| download_result_video | HTTP Request |
| upload_video | Google Drive |
| send_completion_msg | Slack |
| narrative_writer | LLM Chain |
| send_narrative_msg | Slack |
| iterate_prompts | 分批处理 |
| set_current_prompt | 数据设置 |
| narrative_parser | 结构化输出解析器 |
| aggregate_video_results | 数据聚合 |



## 功能说明

AI 视频生成工作流，自动创作视频内容（Viral)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：23
- 触发方式：表单提交触发

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：15
- 输出节点：7
- 分类：devops
