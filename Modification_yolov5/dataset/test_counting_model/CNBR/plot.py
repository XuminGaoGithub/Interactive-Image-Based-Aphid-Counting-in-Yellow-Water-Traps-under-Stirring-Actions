import matplotlib.pyplot as plt
import numpy as np

# 定义数据
C_avg = np.array([0.77571831, 0.75933033, 0.76137611, 0.77618475, 0.76772149, 0.74811876, 0.77535238, 0.78717103, 0.78575156])
N_avg = np.array([9.42857143, 9.28571429, 12.14285714, 9.85714286, 9.71428571, 12.28571429, 13.0, 11.0, 8.42857143])
M_avg = np.array([15.777804, 15.39956339, 14.60387252, 14.35797868, 15.01695548, 15.35049773, 14.75844065, 14.66751578, 14.39954642])
R_avg = np.array([0.4767422, 0.59487026, 0.34868553, 0.44880952, 0.32519008, 0.44904762, 0.4835089, 0.39537037, 0.44869948])

# 时间轴数据 (单位: 秒)
T = np.arange(0, len(C_avg) * 2, 2)  # 以2秒为间隔生成时间点

# 创建绘图
plt.figure(figsize=(12, 8))

# 绘制每个变量随时间的变化
plt.plot(T, C_avg, marker='o', label='C_avg', color='blue')
plt.plot(T, N_avg, marker='o', label='N_avg', color='green')
plt.plot(T, M_avg, marker='o', label='M_avg', color='red')
plt.plot(T, R_avg, marker='o', label='R_avg', color='purple')

# 设置图表的标题和标签
#plt.title('Variables over Time', fontsize=16)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Value', fontsize=14)

# 调整x轴和y轴刻度的字体大小
plt.tick_params(axis='both', which='major', labelsize=12)

# 增加右边界以适应图例
plt.subplots_adjust(right=0.75)  # 增加右边界

# 设置图例位置，放置到x轴和y轴的范围内的右上角
plt.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

# 显示图表
plt.show()

