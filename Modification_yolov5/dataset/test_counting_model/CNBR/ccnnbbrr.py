# -*- coding: utf-8 -*-
import re
import numpy as np

# 读取 sorted_CNBR.txt 文件
with open('sorted_CNBR.txt', 'r') as file:
    lines = file.readlines()

# 用于存储 C, N, B, R 的二维数组
CC, NN, BB, RR = [], [], [], []

# 存储当前组名，确保每组数据是独立的
current_group = None
group_data_C, group_data_N, group_data_B, group_data_R = [], [], [], []

# 遍历文件中的每一行
for line in lines:
    line = line.strip()
    # 匹配图片名称和C, N, B, R值 (例如 5_23_4_fast_0.jpg,0.7498521208763123,5,23.076737663132064,0.25)
    match = re.match(r'(\d+_\d+_\d+).*\.jpg,([0-9.]+),(\d+),([0-9.]+),([0-9.]+)', line)
    if match:
        group = match.group(1)  # 组名 (如 5_23_4)
        C = float(match.group(2))  # C值
        N = int(match.group(3))    # N值
        B = float(match.group(4))  # B值
        R = float(match.group(5))  # R值

        # 如果遇到新的组，保存上一组的数据
        if group != current_group and current_group is not None:
            CC.append(group_data_C)
            NN.append(group_data_N)
            BB.append(group_data_B)
            RR.append(group_data_R)
            group_data_C, group_data_N, group_data_B, group_data_R = [], [], [], []

        # 更新当前组名
        current_group = group

        # 添加数据到当前组
        group_data_C.append(C)
        group_data_N.append(N)
        group_data_B.append(B)
        group_data_R.append(R)

# 处理最后一组的数据
if group_data_C:
    CC.append(group_data_C)
    NN.append(group_data_N)
    BB.append(group_data_B)
    RR.append(group_data_R)

# 将结果转换为numpy数组并打印
CC = np.array(CC)
NN = np.array(NN)
BB = np.array(BB)
RR = np.array(RR)

print("CC (C values):")
print(CC)

print("\nNN (N values):")
print(NN)

print("\nBB (B values):")
print(BB)

print("\nRR (R values):")
print(RR)

