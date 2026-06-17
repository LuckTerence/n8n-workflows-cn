# Run Apache Airflow DAG and Retrieve XCom Value

https://n8nworkflows.xyz/workflows/3026

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

## 触发方式
- in data 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
