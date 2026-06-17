## 简介
**Simple Eval for Legal Benchmarking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4712

---

# Simple Eval for Legal Benchmarking


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Extract from File | 从文件提取 |
| Google Drive | Google Drive |
| Get Tests | Google Sheets |
| Structured Output Parser | 结构化输出解析器 |
| Update Results | Google Sheets |
| LLM Judge | LLM Chain |
| Is PDF? | IF 判断 |
| Is a file? | IF 判断 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
