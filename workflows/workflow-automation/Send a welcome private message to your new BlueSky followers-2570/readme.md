## 简介
**Send a welcome private message to your new BlueSky followers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：14 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2570

---

# Send a welcome private message to your new BlueSky followers


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Session | HTTP Request |
| List followers | HTTP Request |
| Convert to File | 转换为文件 |
| Extract from File | 从文件提取 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| Find new followers | Code |
| Read followers from file | 读写文件 |
| Save followers to file | 读写文件 |
| Define welcome message | 数据设置 |
| Send message | HTTP Request |
| Get conversation ID | HTTP Request |
| Each 60 minutes | 定时触发器 |
| No Operation, do nothing | 空操作 |

## 触发方式
- Each 60 minutes 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：10
- 输出节点：4
- 分类：workflow-automation
