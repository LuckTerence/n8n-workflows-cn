# Analyze Meta Ads Creatives with Google Vision & Video Intelligence APIs

https://n8nworkflows.xyz/workflows/7303

## 节点清单

| 节点 | 类型 |
|------|------|
| Run Daily at 9 AM | 定时触发器 |
| Get Active Ads | facebookGraphApi |
| Is it a Video? | IF 判断 |
| Get Video Source URL | facebookGraphApi |
| Download Video File | HTTP Request |
| Set Campaign ID | 数据设置 |
| Split Out | 数据拆分 |
| Start Video Annotation | HTTP Request |
| If Ready | IF 判断 |
| Parse data | Code |
| Download Image File | HTTP Request |
| Video to Base64 String | 从文件提取 |
| Image to Base64 String | 从文件提取 |
| Start Image Annotation | HTTP Request |
| Set id data for Static | 数据设置 |
| Set id data for Video | 数据设置 |
| Parse data from images | Code |
| Has image_url? | IF 判断 |
| Loop for videos | 分批处理 |
| Add errors | Google Sheets |
| Check Operation Status | HTTP Request |
| Add Segments data | Google Sheets |
| Set (Video Error Row) | 数据设置 |
| Wait 3s | 等待 |
| Wait 30s | 等待 |
| Set (Error Row) | 数据设置 |

## 触发方式
- Run Daily at 9 AM 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
