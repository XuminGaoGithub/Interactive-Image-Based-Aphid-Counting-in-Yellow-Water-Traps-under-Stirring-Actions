import matplotlib.pyplot as plt
import numpy as np

# Data
#5_23_5
#R_gt = np.array([1.0, 0.33333333, 0.52941176, 0.3125, 0.46153846, 0.36842105, 0.58333333, 0.4, 0.25])
#R_pred = np.array([0.5963834, 0.88179704, 0.0878809, 0.51148072, -0.19668057, 0.29845181, 0.6216197, 0.31826394, 0.57760775])

#6_19_5_108MP
R_gt = np.array([0.5625, 0.70588235, 0.6875, 0.5, 0.6, 0.66666667, 0.91304348, 0.57142857, 0.72727273])
R_pred = np.array([0.38345072, 1.11460091, 0.29564255, 0.55113297, -0.11105107, 0.34364285, 0.58364833, 0.20125352, 0.47143211])

#7_3_8
R_gt = np.array([0.30769231, 0.6, 0.38461538, 0.5, 0.47826087, 0.42857143, 0.44444444, 0.625, 0.625])
R_pred = np.array([0.29575269, 1.02891118, 0.27206036, 0.78961751, 0.01501772, 0.41387908, 0.7399687, 0.27796342, 0.44948655])




# Plot
plt.figure(figsize=(8, 5))
plt.plot(R_gt, label='R_gt', marker='o')
plt.plot(R_pred, label='R_pred', marker='s')

# Customize the plot
plt.title("Comparison of R_gt and R_pred", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.legend(fontsize=10)
plt.grid(False)  # Omitting grid lines as per user's preference

# Show the plot
plt.show()
