#!/usr/bin/env python3
"""
将生成的人物数据合并到 mockData.ts
"""
import re

# 读取生成的数据
with open('scripts/generated-people-batch1.ts', 'r', encoding='utf-8') as f:
    gen_content = f.read()

# 提取人物对象
people_match = re.search(r'export const newPeople = \[(.*?)\];', gen_content, re.DOTALL)
if not people_match:
    print("未找到生成的数据")
    exit(1)

new_people_str = people_match.group(1).strip()
# 去掉末尾的逗号
if new_people_str.endswith(','):
    new_people_str = new_people_str[:-1]

# 读取mockData.ts
with open('src/data/mockData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 people 数组开始位置
start = content.find('export const people')
if start == -1:
    print("未找到 people 数组")
    exit(1)

# 从 start 开始找最后一个 \n];\n
# 这标志着 people 数组的结束
end_marker = '\n];\n'
end = content.rfind(end_marker, start)
if end == -1:
    print("未找到 people 数组结尾")
    exit(1)

# 插入位置在 \n]; 的 ] 之后（即换行之前）
# content[end] 是 \n，content[end+1] 是 ]
insert_pos = end + 1 + len('];')  # 指向 \n];\n 中 \n 的位置

before = content[:insert_pos]
after = content[insert_pos:]

new_content = before + ',\n' + new_people_str + after

# 写回
with open('src/data/mockData.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"成功添加新人物到 mockData.ts")
