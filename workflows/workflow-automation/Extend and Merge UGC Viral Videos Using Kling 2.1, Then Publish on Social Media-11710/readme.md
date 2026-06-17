## 简介
**Extend and Merge UGC Viral Videos Using Kling 2.1, Then Publish on Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11710

---

# Extend and Merge UGC Viral Videos Using Kling 2.1, Then Publish on Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Completed?1 | IF 判断 |
| Get Last frame | HTTP Request |
| Update video url | Google Sheets |
| Extract last frame | HTTP Request |
| Wait 10 sec. | 等待 |
| Get status Extract Frame | HTTP Request |
| Set params | 数据设置 |
| Completed?5 | IF 判断 |
| Upload Video2 | Google Drive |
| Generate clip | HTTP Request |
| Get status clip | HTTP Request |
| Wait 60 sec. | 等待 |
| Completed? | IF 判断 |
| Set VideoUrls Json | Code |
| Get videos to merge | Google Sheets |
| Get final video file | HTTP Request |
| Get status | HTTP Request |
| Get final video url | HTTP Request |
| Update video url2 | Google Sheets |
| Wait 30 sec. | 等待 |
| Merge Videos | HTTP Request |
| Upload to Postiz | HTTP Request |
| Upload to Social | postiz |
| Upload to Youtube | HTTP Request |
| Get video | Google Sheets |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：14
- 输出节点：11
- 分类：workflow-automation
