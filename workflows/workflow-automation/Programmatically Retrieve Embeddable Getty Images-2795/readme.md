# Programmatically Retrieve Embeddable Getty Images

https://n8nworkflows.xyz/workflows/2795

## 节点清单

| 节点 | 类型 |
|------|------|
| Parse results page for first image | HTML |
| Continue if a result exists | IF 判断 |
| Extract the Getty image_id from url | 数据设置 |
| Get photo details | HTTP Request |
| GET img src | HTML |
| Get Embeddable iframeSnippet | 数据设置 |
| Request Getty Images Embed code | HTTP Request |
| Raise error when no results | 停止并报错 |
| Replace with CMS node | 空操作 |
| Getty Images Editorial Search | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Replaceable input | 数据设置 |
| Preview image (view binary) | HTTP Request |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
