# Search and download torrents using transmission-daemon

https://n8nworkflows.xyz/workflows/1381

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| SearchTorrent | functionItem |
| Start download | HTTP Request |
| IF | IF 判断 |
| Torrent not found | Telegram |
| Telegram1 | Telegram |
| IF2 | IF 判断 |
| Start download new token | HTTP Request |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
