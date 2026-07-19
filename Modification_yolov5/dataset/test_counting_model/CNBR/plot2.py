import matplotlib.pyplot as plt
import numpy as np

# 定义数据
C_avg = np.array([0.77571831, 0.75933033, 0.76137611, 0.77618475, 0.76772149, 0.74811876, 0.77535238, 0.78717103, 0.78575156])
N_avg = np.array([9.42857143, 9.28571429, 12.14285714, 9.85714286, 9.71428571, 12.28571429, 13.0, 11.0, 8.42857143])
G_avg = np.array([15.777804, 15.39956339, 14.60387252, 14.35797868, 15.01695548, 15.35049773, 14.75844065, 14.66751578, 14.39954642])
R_avg = np.array([0.4767422, 0.59487026, 0.34868553, 0.44880952, 0.32519008, 0.44904762, 0.4835089, 0.39537037, 0.44869948])

# 时间轴数据 (单位: 秒)
T = np.arange(0, len(C_avg) * 2, 2)  # 以2秒为间隔生成时间点

# 绘制第一个图表：C_avg, N_avg, B_avg
plt.figure(figsize=(12, 8))
plt.plot(T, C_avg, marker='o', label='C_avg', color='blue')
plt.plot(T, N_avg, marker='o', label='N_avg', color='green')
plt.plot(T, G_avg, marker='o', label='G_avg', color='red')

# 增大 y 轴范围
plt.ylim(bottom=min(C_avg.min(), N_avg.min(), G_avg.min()) - 1, 
         top=max(C_avg.max(), N_avg.max(), G_avg.max()) + 1)

# 设置第一个图表的标题和标签
#plt.title('C_avg, N_avg, B_avg over Time', fontsize=16)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)

# 将图例放置在右上角
plt.legend(fontsize=12, loc='upper right')

# 显示第一个图表
plt.tight_layout()
plt.show()

# 绘制第二个图表：R_avg
plt.figure(figsize=(12, 8))
plt.plot(T, R_avg, marker='o', label='R_avg', color='purple')

# 增大 y 轴范围
plt.ylim(bottom=R_avg.min() - 0.1, top=R_avg.max() + 0.1)

# 设置第二个图表的标题和标签
#plt.title('R_avg over Time', fontsize=16)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)

# 将图例放置在右上角
plt.legend(fontsize=12, loc='upper right')

# 显示第二个图表
plt.tight_layout()
plt.show()


