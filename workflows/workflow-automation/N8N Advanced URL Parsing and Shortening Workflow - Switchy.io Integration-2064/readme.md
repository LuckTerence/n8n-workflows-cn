# N8N Advanced URL Parsing and Shortening Workflow - Switchy.io Integration

https://n8nworkflows.xyz/workflows/2064

## 节点清单

| 节点 | 类型 |
|------|------|
| Split In Batches | 分批处理 |
| Get Headers | HTTP Request |
| OpenGraph API | HTTP Request |
| Meta tags Scraper - dub.sh | HTTP Request |
| IF OpenGraph invaild | IF 判断 |
| Parse headers | HTML |
| If - Enable ScreenShots (yes to enable) | IF 判断 |
| API Auth | 数据设置 |
| Method 1 - META | 数据设置 |
| Convert to File | 转换为文件 |
| Final Data | 数据设置 |
| CREATE | HTTP Request |
| UPDATE | HTTP Request |
| IF Slug available | IF 判断 |
| Final Meta | 数据聚合 |
| Host Screenshot | github |
| Host OGImage | github |
| Host Favicon | github |
| Edit Fields | 数据设置 |
| Download final OG | HTTP Request |
| Download Favicon | HTTP Request |
| Method 2 - META | 数据设置 |
| Stop and Error | 停止并报错 |
| Method 3 - META1 | 数据设置 |
| Method 1 - SCR | HTTP Request |
| Method 2 - SCR | HTTP Request |
| Final SCR | 数据聚合 |
| Stop And Error | 停止并报错 |
| Shortened URL | 数据设置 |
| n8n Form Trigger | 表单触发器 |
| Respond to Webhook | 响应 Webhook |
| Scan URL (Community) | HTTP Request |
| If | IF 判断 |
| If1 | IF 判断 |
| Check Reviews (Community) | HTTP Request |
| Norton | 数据设置 |
| bitdefender | 数据设置 |
| HTML | HTML |
| (Fraud Check) | HTTP Request |
| (Others) | HTTP Request |
| If2 | IF 判断 |
| set unsafe | 数据设置 |
| If3 | IF 判断 |
| PhishTank | HTTP Request |
| IF GH invaild | IF 判断 |
| Method 4 - META | 数据设置 |
| IF dub invaild | IF 判断 |

## 触发方式
- n8n Form Trigger 触发

## 统计
- 节点总数：47
- 触发节点：1
- 处理节点：31
- 输出节点：15
- 分类：workflow-automation
