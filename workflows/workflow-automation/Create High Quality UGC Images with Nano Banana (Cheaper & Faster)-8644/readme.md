## 简介
**Create High Quality UGC Images with Nano Banana (Cheaper & Faster)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8644

---

# Create High Quality UGC Images with Nano Banana (Cheaper & Faster)


## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Cloud Chat Model | Mistral Chat Model |
| Generate Image | HTTP Request |
| Google Drive Trigger | Google Drive 触发器 |
| Loop Over Items | 分批处理 |
| Upload file | Google Drive |
| Structured Output Parser | 结构化输出解析器 |
| No Operation, do nothing | 空操作 |
| Retrieve Image | HTTP Request |
| Setup | 数据设置 |
| Generate Prompts | LLM Chain |
| Split Out | 数据拆分 |

## 触发方式
- Google Drive Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：8
- 输出节点：2
- 分类：workflow-automation
