## 简介
**DevOps Infrastructure Automation with Docker, K8s, Jenkins & Grafana for Linux Servers**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6140

---

# DevOps Infrastructure Automation with Docker, K8s, Jenkins & Grafana for Linux Servers


## 节点清单

| 节点 | 类型 |
|------|------|
| Start DevOps Setup | 手动触发 |
| Configure Parameters | 数据设置 |
| System Preparation | SSH |
| Install Docker | SSH |
| Install Kubernetes | SSH |
| Install Jenkins | SSH |
| Install Monitoring | SSH |
| Create DevOps User | SSH |
| Security Configuration | SSH |
| Final Configuration | SSH |
| Setup Complete | 数据设置 |
| Wait | 等待 |



## 功能说明

自动部署流水线，代码提交后自动构建和发布。

手动触发，通过 工作流编排 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- Start DevOps Setup 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：devops
