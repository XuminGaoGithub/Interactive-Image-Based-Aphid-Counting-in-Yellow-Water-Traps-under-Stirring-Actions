# -*- coding: utf-8 -*-
import re
import numpy as np

# 读取 sorted_CNBR.txt 文件
with open('sorted_CNBR_training.txt', 'r') as file:
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

# 将结果转换为numpy数组
CC = np.array(CC)
NN = np.array(NN)
BB = np.array(BB)
RR = np.array(RR)

# 定义归一化函数
def min_max_normalization(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    if max_val - min_val == 0:
        return arr  # 如果所有值相等，保持原样
    return (arr - min_val) / (max_val - min_val)

# 计算每列的平均值，得到C', N', B', R'
C_avg = np.mean(CC, axis=0)
N_avg = np.mean(NN, axis=0)
B_avg = np.mean(BB, axis=0)
R_avg = np.mean(RR, axis=0)

print('C_avg:',C_avg)
print('N_avg:',N_avg)
print('B_avg:',B_avg)
print('R_avg:',R_avg)

# 对C', N', B', R'进行Min-Max归一化
C_normalized = min_max_normalization(C_avg)
N_normalized = min_max_normalization(N_avg)
B_normalized = min_max_normalization(B_avg)
R_normalized = min_max_normalization(R_avg)

# 打印归一化后的结果
print("Normalized C' (average C values):")
print(C_normalized)

print("\nNormalized N' (average N values):")
print(N_normalized)

print("\nNormalized B' (average B values):")
print(B_normalized)

print("\nNormalized R' (average R values):")
print(R_normalized)



