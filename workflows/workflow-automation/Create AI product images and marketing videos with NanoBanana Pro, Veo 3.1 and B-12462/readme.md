## 简介
**Create AI product images and marketing videos with NanoBanana Pro, Veo 3.1 and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12462

---

# Create AI product images and marketing videos with NanoBanana Pro, Veo 3.1 and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Image URL | 数据设置 |
| Download Image | HTTP Request |
| Crop Top Left | 图片编辑 |
| Crop Top Center | 图片编辑 |
| Crop Top Right | 图片编辑 |
| Crop Bottom Left | 图片编辑 |
| Crop Bottom Center | 图片编辑 |
| Crop Bottom Right | 图片编辑 |
| Upload to Google Drive | Google Drive |
| Edit Image | 图片编辑 |
| Upload to Google Drive1 | Google Drive |
| Upload to Google Drive2 | Google Drive |
| Upload to Google Drive3 | Google Drive |
| Upload to Google Drive4 | Google Drive |
| Upload to Google Drive5 | Google Drive |
| Update url image_top_left | Google Sheets |
| Update url image_top_center | Google Sheets |
| Update url image_top_right | Google Sheets |
| Update url image_bottom_left | Google Sheets |
| Update url image_bottom_center | Google Sheets |
| Update url image_bottom_right | Google Sheets |
| Schedule Trigger | 定时触发器 |
| Merge1 | 数据合并 |
| Veo Generation | HTTP Request |
| Merge2 | 数据合并 |
| Veo Generation1 | HTTP Request |
| Merge3 | 数据合并 |
| Veo Generation2 | HTTP Request |
| Merge4 | 数据合并 |
| Veo Generation3 | HTTP Request |
| Merge5 | 数据合并 |
| Veo Generation4 | HTTP Request |
| Update video 2 | Google Sheets |
| Update video 5 | Google Sheets |
| Update video 4 | Google Sheets |
| Update video 3 | Google Sheets |
| Update video 1 | Google Sheets |
| Wait: Merge Process | 等待 |
| Merge 3 Videos | HTTP Request |
| Update URL Final video | Google Sheets |
| Wait | 等待 |
| Wait1 | 等待 |
| Wait2 | 等待 |
| Wait3 | 等待 |
| Wait4 | 等待 |
| Merge6 | 数据合并 |
| Search new image | Google Sheets |
| Upload Video to BLOTATO | Blotato |
| Youtube | Blotato |
| Form Trigger (3 images) | 表单触发器 |
| Validate inputs | IF 判断 |
| Error Response - Missing Files | 数据设置 |
| Normalize binary names | 数据设置 |
| Split images | Code |
| OpenAI Vision – Image 1 | OpenAI |
| Aggregate descriptions | Code |
| LLM: Structured Output Parser | 结构化输出解析器 |
| LLM: OpenAI Chat | OpenAI Chat Model |
| Generate Image Prompt | AI Agent |
| NanoBanana: Create Image | HTTP Request |
| Wait for Image Edit | 等待 |
| Download Edited Image | HTTP Request |
| Upload file | Google Drive |
| Merge | 数据合并 |
| Append row in sheet | Google Sheets |
| When clicking ‘Execute workflow’ | 手动触发 |
| Get image nanobanana | Google Sheets |
| Wait for Image Edit1 | 等待 |
| Download Edited Image1 | HTTP Request |
| NanoBanana: Contact Sheet | HTTP Request |
| Edit Fields : contactSheetPrompt | 数据设置 |
| Update database | Google Sheets |

## 触发方式
- Schedule Trigger 触发
- Form Trigger (3 images) 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：72
- 触发节点：3
- 处理节点：58
- 输出节点：11
- 分类：workflow-automation
