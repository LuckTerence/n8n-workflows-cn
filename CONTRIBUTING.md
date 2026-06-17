# 贡献指南

感谢你对 n8n-workflows-cn 的关注！这份指南将帮助你完成第一个贡献。

## 目录

- [贡献方式](#贡献方式)
- [工作流贡献规范](#工作流贡献规范)
- [提交 PR 流程](#提交-pr-流程)
- [代码规范](#代码规范)
- [沟通渠道](#沟通渠道)

## 贡献方式

有多种方式可以参与贡献：

| 方式 | 说明 |
|------|------|
| **新增工作流适配** | 将新的海外服务工作流替换为国内方案 |
| **修复兼容性问题** | 修复已有工作流在新版本 n8n 中的兼容性问题 |
| **完善中文文档** | 补充 readme.md 中的使用说明、节点解析 |
| **提升适配等级** | 将 Tier C/B 的工作流提升到 Tier A |
| **报告 Bug** | 通过 Issue 报告工作流中遇到的问题 |

## 工作流贡献规范

### 文件结构

每个工作流必须包含以下文件，放在对应分类目录下：

```
workflows/{分类}/{工作流名称}-{ID}/
  workflow.json    # 工作流定义文件（必需）
  readme.md        # 节点说明与适配记录（必需）
```

### workflow.json 规范

**必须包含 `_cn_meta` 字段**：

```json
"_cn_meta": {
  "title_zh": "工作流中文名称",
  "description_zh": "用中文简要描述该工作流的功能（一句话）",
  "category": "分类目录名（如 ai-agent、devops 等）",
  "tier": "A",
  "source_id": 12345,
  "synced_at": "2026-06-17T12:00:00"
}
```

**Tier 等级定义**：

| 等级 | 含义 | 标准 |
|:----:|------|------|
| **A** | 完全适配 | 所有节点均替换为国内服务，导入后仅需配置 API Key 即可运行 |
| **B** | 核心可用 | 主要功能链路可用，部分次要节点可能需要自行配置 |
| **C** | 框架适配 | 完成了海外节点的替换框架，但具体参数需要根据实际场景调整 |

**适配原则**：

1. 优先使用 n8n 内置节点（如 OpenAI Chat Model、Email 等）而非全部改为 HTTP Request
2. 保留原始节点结构，仅修改必要的连接参数（Base URL、API Key 等）
3. 不要删除原始节点的注释或描述
4. 测试导入无报错后再提交

### readme.md 规范

```markdown
# 工作流中文名称

原始来源：https://n8nworkflows.xyz/workflows/{source_id}

## 节点清单

| 节点 | 类型 | 适配说明 |
|------|------|----------|
| When chat message received | Chat 触发器 | 无需修改 |
| OpenAI Chat Model | OpenAI Chat Model | 替换为 DeepSeek (base_url + model) |
| AI Agent | AI Agent | 无需修改 |

## 触发方式
- [描述工作流的触发条件]

## 配置说明
- 需要配置的 API Key 或凭证
- 特殊的环境变量或依赖

## 适配记录
- 原始节点: xxx
- 替换节点: yyy
- 修改原因: zzz

## 统计
- 节点总数：N
- 触发节点：N
- 处理节点：N
```

## 提交 PR 流程

### 1. Fork 并 Clone

```bash
git clone https://github.com/YOUR_USERNAME/n8n-workflows-cn.git
cd n8n-workflows-cn
```

### 2. 创建分支

```bash
git checkout -b feat/add-xxx-workflow
```

分支命名规范：
- `feat/` — 新增工作流或功能
- `fix/` — 修复 Bug
- `docs/` — 文档更新
- `tier/` — 提升适配等级

### 3. 提交变更

```bash
git add .
git commit -m "feat(ai-agent): 新增 AI Agent 聊天工作流适配"

# 或
git commit -m "fix(devops): 修复飞书 Webhook 消息体格式"

# 或
git commit -m "tier(finance): 将股票分析工作流从 B 提升到 A"
```

Commit 信息规范（Conventional Commits）：
```
<type>(<scope>): <description>

type: feat | fix | docs | tier | chore
scope: ai-agent | devops | multimodal-ai | knowledge-rag | finance-analysis | workflow-automation
```

### 4. 推送并创建 PR

```bash
git push origin feat/add-xxx-workflow
```

然后在 GitHub 上创建 Pull Request。

### 5. PR 检查清单

在提交 PR 前，请确保：

- [ ] 工作流可以在 n8n 中成功导入（Import from File 无报错）
- [ ] `_cn_meta` 字段完整且正确
- [ ] `readme.md` 包含节点清单和适配记录
- [ ] 目录结构符合规范
- [ ] Tier 等级评定准确
- [ ] 已在 INDEX.md 中添加新工作流条目（如适用）

## 代码规范

- 文件编码：UTF-8
- 缩进：2 空格
- JSON 文件末尾保留一个换行符
- Markdown 文档使用中文
- 工作流名称使用原始英文名 + 中文说明

## 沟通渠道

- **Issue**：报告 Bug 或提出功能建议
- **Discussion**：讨论技术方案和适配思路
- **Pull Request**：提交代码变更

---

再次感谢你的贡献！
