## 简介
**Generate ASMR Rainforest Videos from Text with Seedream & Seedance on fal.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10433

---

# Generate ASMR Rainforest Videos from Text with Seedream & Seedance on fal.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| manual-workflow | 手动触发 |
| create-image | HTTP Request |
| wait-10s | 等待 |
| get-status-image | HTTP Request |
| is-image-complete | IF 判断 |
| create-video | HTTP Request |
| wait-30s | 等待 |
| get-status-video | HTTP Request |
| is-video-complete | IF 判断 |
| link-video | HTTP Request |
| prompt | 数据设置 |
| download-video | HTTP Request |
| link-image | HTTP Request |

## 触发方式
- manual-workflow 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：5
- 输出节点：7
- 分类：workflow-automation
