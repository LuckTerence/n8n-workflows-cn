# 3D Product Video Generator from 2D Image for E-Commerce Stores

https://n8nworkflows.xyz/workflows/4987

## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| On Form Submission | 表单触发器 |
| Give Access to folder | Google Drive |
| Get Image File | Code |
| Upload Remove BG image | Google Drive |
| Extract Image ID from URL | Code |
| Upload Video | Google Drive |
| Create Folder | Google Drive |
| Create Slug | Code |
| Create Video | HTTP Request |
| Check Video Status | HTTP Request |
| Get Video Link | HTTP Request |
| Remove Image Background | HTTP Request |
| Upload Original Image | Google Drive |
| Insert New Product | Google Sheets |
| Update Remove BG URL | Google Sheets |
| Is In Progress | IF 判断 |
| Convert to Binary File | HTTP Request |
| Update Video Link | Google Sheets |
| Send E-Mail Notification | Email 发送 |

## 触发方式
- On Form Submission 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：13
- 输出节点：6
- 分类：workflow-automation
