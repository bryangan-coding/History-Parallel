# 历史平行线 - 数据增扩安全协议

> 本文档用于指导 AI（如 DeepSeek）在进行历史人物/事件数据增扩时，避免重复插入、破坏文件结构等问题。

## 🚨 核心原则

1. **先检查，后生成** - 生成新数据前，必须先确认目标 ID 是否已存在
2. **先预览，后合并** - 合并前使用 `--dry-run` 预览结果
3. **强制 TypeScript 检查** - 合并后必须运行 `tsc --noEmit` 验证
4. **绝不手动修改 `mockData.ts` 结构** - 使用脚本合并，不要直接编辑

## 📋 标准工作流程

### 步骤 1：获取现有 ID 列表（生成前）

```bash
# 列出所有已存在的 person ID
python3 scripts/check-existing-ids.py --list-all > existing_ids.txt
```

**DeepSeek 指令**：
> 在生成任何新人物之前，先运行上述命令获取现有 ID 列表。生成的人物 ID 必须与列表中的 ID 完全不同。如果名称相似，使用不同的 slug（如 `caesar` vs `julius-caesar`）。

### 步骤 2：生成新人物数据

生成符合以下要求的数据文件：
- 文件格式：TypeScript (`export const newPeople = [...]`)
- 字段完整：必须包含 `Person` 接口的所有必填字段
- ID 唯一：与 `existing_ids.txt` 中的 ID 完全不重复
- 英文转义：英文描述中的单引号必须转义为 `\'`

### 步骤 3：预检 ID 重复

```bash
# 检查生成的新数据是否有重复 ID
python3 scripts/check-existing-ids.py --file /tmp/new_people.ts
```

如果输出显示有重复，**必须**删除重复项后再继续。

### 步骤 4：安全合并

```bash
# 预览模式（不实际写入）
python3 scripts/safe-merge-people.py /tmp/new_people.ts --dry-run

# 正式合并（如果有重复会自动跳过）
python3 scripts/safe-merge-people.py /tmp/new_people.ts --force
```

### 步骤 5：验证

合并脚本会自动运行 TypeScript 检查。如果报错：
1. 不要手动修改 `mockData.ts`
2. 从 `git` 恢复文件：`git checkout src/data/mockData.ts`
3. 修正生成数据的问题，重新执行步骤 3-5

## ⚠️ 常见错误与预防

| 错误 | 原因 | 预防方法 |
|------|------|----------|
| React key 重复 | 插入了已有 ID | 步骤 3 预检 |
| TypeScript 结构破坏 | 手动编辑或脚本 bug | 只使用 `safe-merge-people.py` |
| 缺少必填字段 | 未对照 `Person` 接口 | 参考现有数据格式 |
| 单引号未转义 | 英文描述中的 `'` | 使用 `"` 包裹或转义为 `\'` |
| 死循环 | 脚本中的 `while` 循环 | 使用 `for` 循环，设定明确终止条件 |

## 📁 文件位置

```
scripts/
  check-existing-ids.py     # ID 预检脚本（生成前必运行）
  safe-merge-people.py      # 安全合并脚本（带自动去重）
  dedup-mockdata.py         # 去重修复脚本（已损坏时急救）
  validate-data.ts          # 数据验证脚本
```

## 🆘 重复数据急救

如果 DeepSeek 已经插入了重复数据导致 React key 错误：

```bash
# 自动检测并删除 people 数组中的重复 ID（保留第一个）
python3 scripts/dedup-mockdata.py

# 运行后必须验证 TypeScript
npx tsc --noEmit
```

**注意**：`dedup-mockdata.py` 使用逐字符解析（计算括号深度），能正确处理嵌套结构，不会破坏文件。

## 🔧 紧急恢复

如果合并后文件损坏：

```bash
# 从 git 恢复（前提是已 commit）
git checkout src/data/mockData.ts

# 或者从备份恢复
cp /tmp/mockData_backup_xxx.ts src/data/mockData.ts
```

## 📊 当前数据规模

- **Person 总数**: ~565（截至 2026-06-02）
- **Event 总数**: ~2,200+
- **Region 总数**: 35
- **Source 总数**: 27

## ✅ DeepSeek 数据增扩检查清单

在提交合并结果前，确认以下事项：

- [ ] 已运行 `check-existing-ids.py` 确认无重复
- [ ] 已使用 `--dry-run` 预览合并结果
- [ ] TypeScript 检查通过（0 错误）
- [ ] 未手动修改 `mockData.ts` 结构
- [ ] 所有必填字段已填充
- [ ] 已备份原始文件（合并前自动完成）
