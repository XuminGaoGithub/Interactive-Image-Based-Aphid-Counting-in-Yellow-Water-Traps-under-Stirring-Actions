import matplotlib.pyplot as plt

# 数据集
#5_23_5
#data_gt = [2, 4, 10, 14, 8, 5, 8, 9, 6, 8, 7, 2, 3]
#data_pre = [3, 5, 13, 14, 16, 14, 10, 16, 16, 15, 10, 4, 3]
#manual_gt = [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]

#5_23_7
#data_gt = [0, 4, 3, 4, 3, 5, 5, 2, 4]
#data_pre = [0, 6, 5, 7, 5, 3, 5, 6, 1]
#manual_gt = [8, 8, 8, 8, 8, 8, 8, 8, 8]


#6_13_6
#data_gt = [4, 3, 3, 3, 2, 1, 3, 1, 3]
#data_pre = [3, 3, 4, 5, 4, 3, 5, 2, 5]
#manual_gt = [5, 5, 5, 5, 5, 5, 5, 5, 5]


#6_27_3
#data_gt = [17, 10, 9, 5, 12, 16, 17, 23, 15, 1]
#data_pre = [18, 16, 9, 9, 17, 24, 25, 23, 17, 20]
#manual_gt = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29]


#7_3_8
data_gt = [8, 8, 7, 5, 15, 6, 4, 6]
data_pre = [10, 11, 11, 12, 18, 10, 8, 6]
manual_gt = [16, 16, 16, 16, 16, 16, 16, 16]

# 生成时间序列
time = [i for i in range(len(data_gt))]

# 绘制图形
plt.figure(figsize=(10, 6))

# 绘制三条曲线
plt.plot(time, data_gt, marker='o', linestyle='-', color='b', label='Label_gt')
plt.plot(time, data_pre, marker='x', linestyle='-', color='r', label='Predict')
plt.plot(time, manual_gt, marker='^', linestyle='--', color='g', label='Manual_gt')

# 设置标题和标签
plt.title('7_3_8', fontsize=16)  # 增大标题字体大小
plt.xlabel('Time (second) x 2', fontsize=16)  # 增大x轴标签字体大小
plt.ylabel('Aphid number', fontsize=16)  # 增大y轴标签字体大小

# 设置x轴和y轴的刻度值
xticks_values = [i for i in range(1, len(data_gt) + 1)]  # 假设x轴刻度值需要乘以2
yticks_values = list(range(min(min(data_gt), min(data_pre), min(manual_gt)), 
                           max(max(data_gt), max(data_pre), max(manual_gt)) + 1, 5))  # 假设y轴刻度值间隔为5

# 设置x轴和y轴的刻度标签字体大小
plt.xticks(xticks_values, fontsize=14)  # 设置x轴刻度标签字体大小
plt.yticks(yticks_values, fontsize=14)  # 设置y轴刻度标签字体大小

# 添加图例
plt.legend(fontsize=14)

# 显示网格
# plt.grid(True)

# 显示图形
plt.show()

