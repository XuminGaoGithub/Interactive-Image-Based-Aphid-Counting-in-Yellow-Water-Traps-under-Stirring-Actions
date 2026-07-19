import matplotlib.pyplot as plt
import numpy as np

# 定义数据
C_avg = np.array([0.77571831, 0.75933033, 0.76137611, 0.77618475, 0.76772149, 0.74811876, 0.77535238, 0.78717103, 0.78575156])
N_avg = np.array([9.42857143, 9.28571429, 12.14285714, 9.85714286, 9.71428571, 12.28571429, 13.0, 11.0, 8.42857143])
G_avg = np.array([15.777804, 15.39956339, 14.60387252, 14.35797868, 15.01695548, 15.35049773, 14.75844065, 14.66751578, 14.39954642])
R_avg = np.array([0.4767422, 0.59487026, 0.34868553, 0.44880952, 0.32519008, 0.44904762, 0.4835089, 0.39537037, 0.44869948])

# 时间轴数据 (单位: 秒)
T = np.arange(0, len(C_avg) * 2, 2)  # 以2秒为间隔生成时间点

# Stirring start and end times
stir_start = 2  # 第二个时刻
stir_end = 8    # 第五个时刻

# Function to add vertical lines and labels
def add_stir_lines():
    plt.axvline(x=stir_start, color='black', linestyle='--')  # 开始搅拌标记
    plt.axvline(x=stir_end, color='black', linestyle='--')    # 结束搅拌标记
    plt.text(stir_start, 0.95, 'stirring start', color='black', fontsize=20, ha='center', transform=plt.gca().get_xaxis_transform())
    plt.text(stir_end, 0.95, 'stirring end', color='black', fontsize=20, ha='center', transform=plt.gca().get_xaxis_transform())

# 绘制第一个图表：C_avg
plt.figure(figsize=(8, 6))
plt.plot(T, C_avg, marker='o', color='blue', label='C_avg')
add_stir_lines()  # 添加搅拌标记
plt.xlabel('Time (s)', fontsize=30)
plt.ylabel('C_avg', fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.tight_layout()
plt.show()

# 绘制第二个图表：N_avg
plt.figure(figsize=(8, 6))
plt.plot(T, N_avg, marker='o', color='green', label='N_avg')
add_stir_lines()  # 添加搅拌标记
plt.xlabel('Time (s)', fontsize=30)
plt.ylabel('N_avg', fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.tight_layout()
plt.show()

# 绘制第三个图表：G_avg
plt.figure(figsize=(8, 6))
plt.plot(T, G_avg, marker='o', color='red', label='G_avg')
add_stir_lines()  # 添加搅拌标记
plt.xlabel('Time (s)', fontsize=30)
plt.ylabel('G_avg', fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.tight_layout()
plt.show()

# 绘制第四个图表：R_avg
plt.figure(figsize=(8, 6))
plt.plot(T, R_avg, marker='o', color='purple', label='R_avg')
add_stir_lines()  # 添加搅拌标记
plt.xlabel('Time (s)', fontsize=30)
plt.ylabel('R_avg', fontsize=30)
plt.tick_params(axis='both', which='major', labelsize=26)
plt.tight_layout()
plt.show()
