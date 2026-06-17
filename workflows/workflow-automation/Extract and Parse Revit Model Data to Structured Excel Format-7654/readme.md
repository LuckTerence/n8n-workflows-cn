# Extract and Parse Revit Model Data to Structured Excel Format

https://n8nworkflows.xyz/workflows/7654

## 节点清单

| 节点 | 类型 |
|------|------|
| Start - Click to begin | 手动触发 |
| Setup - Define file paths | 数据设置 |
| Extract - Run Revit converter | 执行命令 |
| Check - Did extraction succeed? | IF 判断 |
| Success - Create Excel filename | 数据设置 |
| Error - Show what went wrong | 数据设置 |
| Extract - Read Excel file from disk | 读取二进制文件 |
| Extract - Parse Excel to data | 电子表格文件 |
| On the standard 3D View | IF 判断 |

## 触发方式
- Start - Click to begin 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
