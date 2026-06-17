## 简介
**Run Apache Airflow DAG and Retrieve XCom Value**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3026

---

# Run Apache Airflow DAG and Retrieve XCom Value


## 节点清单

| 节点 | 类型 |
|------|------|
| Airflow: dag_run | HTTP Request |
| Airflow: dag_run - state | HTTP Request |
| count | Code |
| dag run fail | 停止并报错 |
| if state == queued | IF 判断 |
| dag run wait too long | 停止并报错 |
| Airflow: dag_run - get result | HTTP Request |
| Switch: state | Switch 路由 |
| in data | 执行工作流触发器 |
| Wait | 等待 |
| If count > wait_time | IF 判断 |
| airflow-api | 数据设置 |



## 功能说明

Run Apache Airflow DAG and Retrieve XCom Value。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：手动或子流程调用

## 触发方式
- in data 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
