import numpy as np
import torch
import torch.nn.functional as F

# 定义数据
#data = np.array([0.5963834, 0.88179704, 0.0878809, 0.51148072, -0.19668057, 
                 #0.29845181, 0.6216197, 0.31826394, 0.57760775])
data = np.array([0.38345072, 1.11460091, 0.29564255, 0.55113297, -0.11105107, 
                   0.34364285, 0.58364833, 0.20125352, 0.47143211])

# 定义 N_avg
#N_avg = np.array([2., 4., 16., 13., 11., 17., 11., 5., 2.])
N_avg = np.array([15., 15., 16., 16., 17., 16., 23., 20., 20.])

# 将数据转换为 Tensor
data_tensor = torch.tensor(data)

# 计算 Softmax 输出
softmax_output = F.softmax(data_tensor, dim=0).cpu().data.numpy()

# 将 Softmax 概率与 N_avg 对应相乘
result = softmax_output * N_avg

# 计算乘积后的总和
final_sum = np.sum(result)

# 输出结果
print("Softmax 概率:", softmax_output)
print("与 N_avg 相乘的结果:", result)
print("最终相加结果:", final_sum)

