## 简介
**Send a welcome private message to your new BlueSky followers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Send a welcome private message to your new BlueSky。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：15
- 触发方式：定时触发

## 触发方式
- Each 60 minutes 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：10
- 输出节点：4
- 分类：workflow-automation
