## 简介
**Prevent Concurrent Workflow Runs Using Redis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：30 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/3976

---

# Prevent Concurrent Workflow Runs Using Redis


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Switch | Switch 路由 |
| When clicking ‘Test workflow’ | 手动触发 |
| If2 | IF 判断 |
| Is Workflow Active | 执行工作流 |
| Set Workflow Active | 执行工作流 |
| Set Workflow Finished | 执行工作流 |
| Get Key | Redis |
| Set Key | Redis |
| UnSet Key | Redis |
| Set Timeout | 数据设置 |
| set continue | 数据设置 |
| If | IF 判断 |
| Is Workflow Active1 | 执行工作流 |
| Stop and Error | 停止并报错 |
| No Operation, do nothing | 空操作 |
| Set Workflow Active1 | 执行工作流 |
| Set Workflow Finished1 | 执行工作流 |
| Wait | 等待 |
| If1 | IF 判断 |
| Is Workflow Active2 | 执行工作流 |
| Stop and Error1 | 停止并报错 |
| Set Workflow Finished2 | 执行工作流 |
| Wait1 | 等待 |
| Wait2 | 等待 |
| Wait3 | 等待 |
| Set Workflow "started" | 执行工作流 |
| Set Workflow "finishing" | 执行工作流 |
| Set Workflow "loading" | 执行工作流 |
| Is Workflow Active3 | 执行工作流 |
| Switch1 | Switch 路由 |

## 触发方式
- When Executed by Another Workflow 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：31
- 触发节点：2
- 处理节点：29
- 输出节点：0
- 分类：workflow-automation
