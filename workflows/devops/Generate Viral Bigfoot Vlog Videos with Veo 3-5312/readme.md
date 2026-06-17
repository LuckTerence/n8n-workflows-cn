# Generate Viral Bigfoot Vlog Videos with Veo 3

https://n8nworkflows.xyz/workflows/5312

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

## 触发方式
- form_trigger 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：15
- 输出节点：7
- 分类：devops
