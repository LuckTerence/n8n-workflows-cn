## 简介
**Auto-Retry Engine: Error Recovery Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3144

---

# Auto-Retry Engine: Error Recovery Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| n8n | n8n |
| Log into n8n | HTTP Request |
| retry workflow automatically | HTTP Request |
| If | IF 判断 |
| No Operation, do nothing | 空操作 |
| login_details | 数据设置 |
| Loop Over Items | 分批处理 |
| Schedule Trigger | 定时触发器 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
