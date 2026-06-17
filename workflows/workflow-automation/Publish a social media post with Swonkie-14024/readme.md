## 简介
**Publish a social media post with Swonkie**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：15 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/14024

---

# Publish a social media post with Swonkie


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Configure | 数据设置 |
| Create Media Entry | HTTP Request |
| Download & Attach Binary | HTTP Request |
| Upload File to Blob | HTTP Request |
| Confirm Upload | HTTP Request |
| Wait for Processing | 等待 |
| Check Media Status | HTTP Request |
| Media Ready? | Switch 路由 |
| Create Post | HTTP Request |
| Validate Post | HTTP Request |
| Post Valid? | IF 判断 |
| Change Stage | HTTP Request |
| Post Published | 数据设置 |
| Media Processing Failed | 停止并报错 |
| Validation Failed | 停止并报错 |

## 触发方式
- Start 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：7
- 输出节点：8
- 分类：workflow-automation
