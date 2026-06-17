## 简介
**Automated Generation of AI Advertising Photos for Product Marketing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3700

---

# Automated Generation of AI Advertising Photos for Product Marketing


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Merge | 数据合并 |
| Read Image URLs | Google Sheets |
| Download Images | HTTP Request |
| Analyze Images | OpenAI |
| Product Photography Prompt | LLM Chain |
| Send Image with Prompt to OpenAI | HTTP Request |
| Convert Base64 to File | 转换为文件 |
| Upload to Drive | Google Drive |
| Insert Image URL in Table | Google Sheets |
| When clicking 'Test workflow' | 手动触发 |
| Convert to File | 转换为文件 |
| Generate Image | HTTP Request |

## 触发方式
- When clicking 'Test workflow' 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
