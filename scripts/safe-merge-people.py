#!/usr/bin/env python3
"""
安全合并人物数据脚本：将新人物数据合并到 mockData.ts，自动去重

特点：
- 合并前自动检查重复 ID
- 保留原始数据，跳过重复项
- 不破坏文件结构
- 合并后自动运行 TypeScript 检查

用法：
  python3 scripts/safe-merge-people.py /tmp/new_people_batch.ts
  python3 scripts/safe-merge-people.py /tmp/new_people_batch.ts --dry-run  # 预览模式
  python3 scripts/safe-merge-people.py /tmp/new_people_batch.ts --force     # 强制合并（跳过重复检查）
"""
import re
import subprocess
import sys
import argparse
from pathlib import Path

MOCKDATA_PATH = Path(__file__).parent.parent / "src" / "data" / "mockData.ts"
PROJECT_ROOT = Path(__file__).parent.parent


def extract_people_ids(content: str) -> set[str]:
    """从 mockData.ts 中提取所有 person ID"""
    people_start = content.find("export const people")
    if people_start == -1:
        return set()

    array_start = content.find("[", people_start)
    events_pos = content.find("export const events", array_start)
    if events_pos == -1:
        return set()

    array_end = content.rfind("];", array_start, events_pos)
    if array_end == -1:
        return set()

    people_array = content[array_start:array_end]
    ids = re.findall(r"id:\s*'([^']+)'", people_array)
    return set(ids)


def extract_persons_from_new_data(content: str) -> list[dict]:
    """从新数据文件中提取 person 对象列表"""
    # 匹配 export const xxx = [ ... ]; 结构
    match = re.search(r"=\s*\[(.*)\];", content, re.DOTALL)
    if not match:
        return []

    persons_text = match.group(1)

    # 使用更精确的匹配：找到每个 { id: 'xxx', ... } 对象
    # 注意：这里使用简单的字符串分割，假设每个对象以 }, 或 } 结尾
    objects = []
    depth = 0
    current = ""
    in_string = False
    string_char = None

    for char in persons_text:
        if char in ('"', "'") and (not current or current[-1] != "\\"):
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None

        if not in_string:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1

        current += char

        if depth == 0 and current.strip() and not in_string:
            obj = current.strip().rstrip(",")
            if obj.startswith("{") and obj.endswith("}"):
                # 提取 id
                id_match = re.search(r"id:\s*'([^']+)'", obj)
                if id_match:
                    objects.append({
                        "id": id_match.group(1),
                        "text": obj,
                    })
            current = ""

    return objects


def merge_people(new_file_path: str, dry_run: bool = False, force: bool = False) -> None:
    """合并新人物到 mockData.ts"""
    # 读取 mockData.ts
    with open(MOCKDATA_PATH, "r", encoding="utf-8") as f:
        mockdata = f.read()

    # 读取新人物数据
    with open(new_file_path, "r", encoding="utf-8") as f:
        new_data = f.read()

    # 提取现有 ID
    existing_ids = extract_people_ids(mockdata)
    print(f"现有 person 总数: {len(existing_ids)}")

    # 提取新人物
    new_persons = extract_persons_from_new_data(new_data)
    if not new_persons:
        print(f"❌ 错误: 无法从 {new_file_path} 提取人物数据")
        sys.exit(1)

    print(f"新数据中的 person 数: {len(new_persons)}")

    # 检查重复
    duplicates = []
    unique_persons = []

    for person in new_persons:
        if person["id"] in existing_ids:
            duplicates.append(person["id"])
        else:
            unique_persons.append(person)

    if duplicates:
        print(f"\n⚠️  发现 {len(duplicates)} 个重复 ID:")
        for pid in duplicates:
            print(f"  ❌ {pid}")

        if not force:
            print(f"\n❌ 合并已取消。请删除重复项后重试，或使用 --force 参数跳过重复项。")
            print(f"   建议: 先运行 python3 scripts/check-existing-ids.py --file {new_file_path}")
            sys.exit(1)
        else:
            print(f"\n⚡ --force 模式: 跳过 {len(duplicates)} 个重复项，合并 {len(unique_persons)} 个新人物")

    if not unique_persons:
        print(f"\n✅ 没有新人物需要合并（全部重复）")
        return

    if dry_run:
        print(f"\n--- 预览模式（不实际写入）---")
        print(f"将新增 {len(unique_persons)} 个人物:")
        for p in unique_persons:
            print(f"  ✅ {p['id']}")
        return

    # 找到 people 数组的插入位置
    # With 2-part split, insert into _peoplePart2
    part2_start = mockdata.find("export const _peoplePart2")
    if part2_start != -1:
        # Find the array in _peoplePart2
        people_start = part2_start
        array_start = mockdata.find("[", part2_start)
        # Find the end of _peoplePart2 array (before next export)
        events_pos = mockdata.find("export const", array_start + 1)
        array_end = mockdata.rfind("];", array_start, events_pos)
    else:
        # Legacy single-array format
        people_start = mockdata.find("export const people")
        array_start = mockdata.find("[", people_start)
        events_pos = mockdata.find("export const events", array_start)
        array_end = mockdata.rfind("];", array_start, events_pos)

    # 构建新的人物文本块
    persons_block = ",\n".join([p["text"] for p in unique_persons])

    # 在 ]; 之前插入
    # 找到最后一个 }, 的位置，在其后添加逗号和新数据
    insert_pos = array_end

    # 检查插入点前面是否需要逗号
    before_insert = mockdata[insert_pos - 10:insert_pos].strip()
    needs_comma = not before_insert.endswith(",")

    separator = ",\n" if needs_comma else "\n"
    new_content = mockdata[:insert_pos] + separator + persons_block + mockdata[insert_pos:]

    # 写入文件
    with open(MOCKDATA_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\n✅ 成功合并 {len(unique_persons)} 个新人物")
    for p in unique_persons:
        print(f"  + {p['id']}")

    # 运行 TypeScript 检查
    print(f"\n🔍 运行 TypeScript 检查...")
    result = subprocess.run(
        ["npx", "tsc", "--noEmit", "--pretty", "false"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        env={**dict(subprocess.os.environ), "NODE_OPTIONS": "--max-old-space-size=12288"},
    )

    if result.returncode == 0:
        print(f"✅ TypeScript 检查通过！0 错误")
    else:
        print(f"❌ TypeScript 检查失败:")
        print(result.stdout[:2000])
        print(f"\n⚠️  请修复上述错误后再提交")


def main():
    parser = argparse.ArgumentParser(description="安全合并人物数据到 mockData.ts")
    parser.add_argument("new_file", help="新人物数据文件路径（TypeScript 格式）")
    parser.add_argument("--dry-run", "-d", action="store_true", help="预览模式，不实际写入")
    parser.add_argument("--force", "-f", action="store_true", help="强制合并，跳过重复项")
    args = parser.parse_args()

    merge_people(args.new_file, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()
