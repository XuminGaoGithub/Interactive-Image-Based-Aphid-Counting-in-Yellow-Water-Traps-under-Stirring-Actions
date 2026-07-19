# -*- coding: utf-8 -*-
import re

# 读取txt文件
with open('cnbr.txt', 'r') as file:
    lines = file.readlines()

# 存储按组分好的数据
grouped_data = {}

# 解析每行数据
for line in lines:
    line = line.strip()  # 去除首尾空白符
    # 使用正则表达式提取组名和序列号（例如5_23_4_fast_1.jpg）
    match = re.match(r'(\d+_\d+_\d+).*_(\d+)\.jpg', line)
    if match:
        group = match.group(1)  # 提取日期时间组 (如 5_23_4)
        sequence = int(match.group(2))  # 提取序列号 (如 1)
        # 将数据按组存储，并以序列号排序
        if group not in grouped_data:
            grouped_data[group] = []
        grouped_data[group].append((sequence, line))

# 对每组数据按序列号排序
for group in grouped_data:
    grouped_data[group].sort(key=lambda x: x[0])

# 输出排序后的结果
with open('sorted_CNBR.txt', 'w') as output_file:
    for group in grouped_data:
        for _, line in grouped_data[group]:
            output_file.write(f"{line}\n")

print("数据已经按照序列号排序并保存到 'sorted_CNBR.txt'")


