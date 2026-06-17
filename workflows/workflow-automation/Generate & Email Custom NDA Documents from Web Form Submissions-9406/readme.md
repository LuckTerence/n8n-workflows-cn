## 简介
**Generate & Email Custom NDA Documents from Web Form Submissions**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9406

---

# Generate & Email Custom NDA Documents from Web Form Submissions


## 节点清单

| 节点 | 类型 |
|------|------|
| Send email | Email 发送 |
| FormData Endpoint | Webhook |
| HTML for Landingpage | HTML |
| Landingpage Endpoint | Webhook |
| Respond to Webhook | 响应 Webhook |
| Set Form Endpoint | 数据设置 |
| HTML to Docx | Html2Docx |
| NDA (HTML Version) | HTML |

## 触发方式
- FormData Endpoint 触发
- Landingpage Endpoint 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
