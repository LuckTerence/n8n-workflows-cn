## 简介
**Generate Product Creative Images with Google Nano-Banana Model via Defapi**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8484

---

# Generate Product Creative Images with Google Nano-Banana Model via Defapi


## 节点清单

| 节点 | 类型 |
|------|------|
| Obtain the generated status | HTTP Request |
| Submit Image for Creative Generation | 表单触发器 |
| Send Image Generation Request to Defapi.org API | HTTP Request |
| Wait for Image Processing Completion | 等待 |
| Check if Image Generation is Complete | IF 判断 |
| Format and Display Image Results | 数据设置 |
| Get Your Balance | HTTP Request |
| Show Balance | 数据设置 |

## 触发方式
- Submit Image for Creative Generation 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
