# FB Ad Spy: AI-Powered Competitor Ad Intelligence & Auto-Video Remixer

https://n8nworkflows.xyz/workflows/15144

## 节点清单

| 节点 | 类型 |
|------|------|
| On Manual Start | 手动触发 |
| Filter by Ad Likes | 过滤器 |
| Wait Before Processing Text Ads | 等待 |
| Wait Before Image Creation | 等待 |
| Download Video Content | HTTP Request |
| Save Video to Google Drive | Google Drive |
| Wait Before Video Processing | 等待 |
| Scrape Ad Library Data | HTTP Request |
| Batch Image Ads Processing | 分批处理 |
| Batch Text Ads Processing | 分批处理 |
| Batch Video Ads Processing | 分批处理 |
| Initiate Gemini Upload | HTTP Request |
| Retrieve Video from Drive | Google Drive |
| Submit Video to Gemini | HTTP Request |
| Analyze Video in Gemini | HTTP Request |
| Summarize Video with AI | OpenAI |
| Record Video Data in Sheets | Google Sheets |
| Analyze Image with AI | OpenAI |
| Summarize Image with AI | OpenAI |
| Record Image Data in Sheets | Google Sheets |
| Summarize Text with AI | OpenAI |
| Record Text Data in Sheets | Google Sheets |
| Wait for Analysis Completion | 等待 |
| Convert Media Into File | 转换为文件 |
| Query Server Status | HTTP Request |
| Start Video Generation Process | HTTP Request |
| Create JWT Token | jwt |
| Obtain OAuth Token | HTTP Request |
| Check Rendering Status | HTTP Request |
| Verify Status OK | IF 判断 |
| Await Rendering Completion | 等待 |
| Download Finalized Video | HTTP Request |
| Save File to Cloud Storage | googleCloudStorage |
| Transform Video to 9:16 Ratio | HTTP Request |
| Verify Captions Presence | IF 判断 |
| Insert Video Captions | HTTP Request |
| Await Caption Completion | 等待 |
| Verify Caption Completion | HTTP Request |
| Evaluate Condition Route | Switch 路由 |
| Pause for 20 Seconds | 等待 |
| Modify Google Sheet Entry | Google Sheets |
| Upload Final Output to Cloud | googleCloudStorage |
| Configure API Parameters | 数据设置 |
| Create Video Prompt with AI | OpenAI |
| Generate Image with AI | OpenAI |
| Apply Filter to Video Ads | 过滤器 |
| Apply Filter to Image Ads | 过滤器 |
| Apply Multi-Condition Filter to Text Ads | 过滤器 |
| Distribute Ad Cards | 数据拆分 |
| Separate Video Resources | 数据拆分 |
| Fetch Image From URL | HTTP Request |
| Extract Batch of Ad Cards | 数据拆分 |
| Filter Ads by Likes | 过滤器 |
| Filter Videos by Likes | 过滤器 |

## 触发方式
- On Manual Start 触发

## 统计
- 节点总数：54
- 触发节点：1
- 处理节点：39
- 输出节点：14
- 分类：workflow-automation
