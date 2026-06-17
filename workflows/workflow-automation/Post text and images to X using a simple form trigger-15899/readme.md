## 简介
**Post text and images to X using a simple form trigger**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：20 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/15899

---

# Post text and images to X using a simple form trigger


## 节点清单

| 节点 | 类型 |
|------|------|
| When Form Submitted | 表单触发器 |
| Normalize Form Input | Code |
| Check Input Validity | IF 判断 |
| Set Input Error Status | 数据设置 |
| Check If Image Exists | IF 判断 |
| Post New Tweet | HTTP Request |
| Check Tweet Status | IF 判断 |
| Set Tweet Error Status | 数据设置 |
| Confirm Post Success | 数据设置 |
| Upload Image to X | HTTP Request |
| Check Image Upload | IF 判断 |
| Set Media Upload Error | 数据设置 |
| Generate Media IDs | Code |
| Verify Media ID Availability | IF 判断 |
| Post Tweet With Media | HTTP Request |
| Check Media Post Status | IF 判断 |
| Confirm Media Post Success | 数据设置 |
| Manual X Connection Test | 手动触发 |
| Fetch X User Info | HTTP Request |
| Check Test Outcome | IF 判断 |
| Record Test Error | 数据设置 |
| Record Test Success | 数据设置 |

## 触发方式
- When Form Submitted 触发
- Manual X Connection Test 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：16
- 输出节点：4
- 分类：workflow-automation
