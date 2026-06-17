# Generate Interactive Wall Quantity Reports from Revit Models to HTML

https://n8nworkflows.xyz/workflows/5869

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
| Transform - Filter only OST_Walls | IF 判断 |
| Transform - Clean wall data | 数据设置 |
| Transform - Group by Type Name & sum Volume | Function |
| Transform - Generate HTML Report | Function |
| Load - Save HTML Report | 写入二进制文件 |
| Success - Final results | 数据设置 |

## 触发方式
- Start - Click to begin 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
