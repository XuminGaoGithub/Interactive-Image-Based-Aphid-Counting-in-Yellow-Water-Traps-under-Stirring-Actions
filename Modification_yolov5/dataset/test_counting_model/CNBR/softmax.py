import numpy as np
import torch
import torch.nn.functional as F

# 原始数据
data = np.array([0.5963834, 0.88179704, 0.0878809, 0.51148072, -0.19668057,
                 0.29845181, 0.6216197, 0.31826394, 0.57760775])

# 转换为 Tensor
data_tensor = torch.tensor(data)

# 计算 Softmax 输出
softmax_output = F.softmax(data_tensor, dim=0).cpu().data.numpy()

# 输出结果
print(softmax_output)
