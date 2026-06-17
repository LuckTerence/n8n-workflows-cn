## 简介
**Automatically Generate Burn-in Video Captions with json2video**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3044

---

# Automatically Generate Burn-in Video Captions with json2video


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| json2video - Add Captions | HTTP Request |
| Config | 数据设置 |
| Wait | 等待 |
| Is Error | IF 判断 |
| Handle Error | 空操作 |
| Output | 数据设置 |
| json2video - Get Status | HTTP Request |
| is Completed | IF 判断 |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
