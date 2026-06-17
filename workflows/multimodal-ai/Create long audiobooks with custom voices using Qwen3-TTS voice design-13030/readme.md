## 简介
**Create long audiobooks with custom voices using Qwen3-TTS voice design**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13030

---

# Create long audiobooks with custom voices using Qwen3-TTS voice design


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Get status | HTTP Request |
| Wait 30 sec. | 等待 |
| Get scripts | Google Sheets |
| Update Temp URL | Google Sheets |
| Set AudioUrls Json | Code |
| Merge Audios | HTTP Request |
| Wait 10 sec. | 等待 |
| Completed? | IF 判断 |
| Get final audio url | HTTP Request |
| Get File | HTTP Request |
| Upload Audiobook | Google Drive |
| Voice Design | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：multimodal-ai
