# Classify & Extract Data from Floorplans with Mistral AI OCR & JigsawStack

https://n8nworkflows.xyz/workflows/8420

## 节点清单

| 节点 | 类型 |
|------|------|
| Check – GDPR Consent | IF 判断 |
| Webhook – Receive Upload | Webhook |
| Respond – Consent Required | 响应 Webhook |
| Process – Multiple File Uploads | Code |
| Check – File Type (PDF/Image) | IF 判断 |
| Extract – PDF Metadata/Text | 从文件提取 |
| Check – File Size & Pages | IF 判断 |
| Analyze – Confidence Score (Heuristics) | Code |
| Route – Confidence Levels | Switch 路由 |
| Respond – Low Quality/Drop | 响应 Webhook |
| Classify – Image Files | HTTP Request |
| Classify – PDF Text | HTTP Request |
| Respond – Classification Result (Image) | 响应 Webhook |
| Respond – Classification Result (PDF) | 响应 Webhook |
| Respond – File Too Large | 响应 Webhook |
| Upload – JigsawStack (Storage) | HTTP Request |
| No Operation, do nothing | 空操作 |

## 触发方式
- Webhook – Receive Upload 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
