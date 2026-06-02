#!/usr/bin/env python3
"""
数据增扩预检脚本：检查指定 ID 是否已存在于 mockData.ts 中

用法：
  python3 scripts/check-existing-ids.py bianque zhangzhongjing caocao
  python3 scripts/check-existing-ids.py --file /tmp/new_people.ts
  python3 scripts/check-existing-ids.py --list-all > existing_ids.txt
"""
import re
import sys
import argparse
from pathlib import Path

MOCKDATA_PATH = Path(__file__).parent.parent / "src" / "data" / "mockData.ts"


def extract_people_ids(content: str) -> set[str]:
    """从 mockData.ts 中提取所有 person ID"""
    # 找到 people 数组的范围
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


def check_ids(ids_to_check: list[str], existing_ids: set[str]) -> None:
    """检查指定 ID 是否已存在"""
    duplicates = []
    new_ids = []

    for pid in ids_to_check:
        if pid in existing_ids:
            duplicates.append(pid)
        else:
            new_ids.append(pid)

    print(f"\n=== ID 预检结果 ===")
    print(f"检查总数: {len(ids_to_check)}")
    print(f"  ✅ 可新增: {len(new_ids)}")
    print(f"  ❌ 已存在: {len(duplicates)}")

    if new_ids:
        print(f"\n--- 可新增的 ID ---")
        for pid in new_ids:
            print(f"  ✅ {pid}")

    if duplicates:
        print(f"\n--- 已存在的 ID（请勿重复插入）---")
        for pid in duplicates:
            print(f"  ❌ {pid}")
        print(f"\n⚠️  警告: 发现 {len(duplicates)} 个重复 ID！")
        print(f"   请删除重复项后再合并，或使用 --skip-duplicates 参数")

    # 返回退出码：有重复则返回 1
    sys.exit(1 if duplicates else 0)


def extract_ids_from_file(file_path: str) -> list[str]:
    """从 TypeScript 文件中提取 person ID"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    ids = re.findall(r"id:\s*'([^']+)'", content)
    return ids


def main():
    parser = argparse.ArgumentParser(description="检查人物 ID 是否已存在于 mockData.ts")
    parser.add_argument("ids", nargs="*", help="要检查的 ID 列表")
    parser.add_argument("--file", "-f", help="从 TypeScript 文件读取 ID")
    parser.add_argument("--list-all", "-l", action="store_true", help="列出所有已存在的 ID")
    args = parser.parse_args()

    # 读取 mockData.ts
    with open(MOCKDATA_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    existing_ids = extract_people_ids(content)

    if args.list_all:
        for pid in sorted(existing_ids):
            print(pid)
        print(f"\n总计: {len(existing_ids)} 个 ID", file=sys.stderr)
        return

    # 获取要检查的 ID
    ids_to_check = []
    if args.file:
        ids_to_check = extract_ids_from_file(args.file)
    elif args.ids:
        ids_to_check = args.ids
    else:
        parser.print_help()
        return

    check_ids(ids_to_check, existing_ids)


if __name__ == "__main__":
    main()
