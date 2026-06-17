## 简介
**Automate Face Swapping for GIFs with Fal.run AI and Google Services**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4450

---

# Automate Face Swapping for GIFs with Fal.run AI and Google Services


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get File image | HTTP Request |
| Get Url image | HTTP Request |
| Get status | HTTP Request |
| Google Sheets | Google Sheets |
| Wait 60 sec. | 等待 |
| Schedule Trigger | 定时触发器 |
| Completed? | IF 判断 |
| Upload Image | Google Drive |
| Update result | Google Sheets |
| Set data | 数据设置 |
| Create Image | HTTP Request |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
