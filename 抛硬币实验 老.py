# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:21:51 2023

@author: Gloria X
"""

import numpy as np
import matplotlib.pyplot as plt
import arrow
start_time = float(arrow.get().format('X'))

def coin_toss():
    # 随机生成一个0或1
    return np.random.choice([-1, 1])

def run_experiment(num_tosses):
    # 存储每次抛硬币的结果，即x
    results = np.empty(num_tosses)
    for i in range(num_tosses):
        results[i] = coin_toss()
    return results

def compute_running_sum(results):
    # 计算前几项结果之和，即y
    running_sum = np.empty(len(results))
    running_sum[0] = results[0]
    for i in range(1, len(results)):
        running_sum[i] = running_sum[i-1] + results[i]
    return running_sum

# 抛n次硬币
num_tosses = 100000000
results = run_experiment(num_tosses)

# 计算前几项结果之和
running_sum = compute_running_sum(results)

# 打印结果
# print("x:", results)
# print("y:", running_sum)

# 生成图像
# x = np.arange(num_tosses)
# plt.plot(x, running_sum)
# plt.title("Running Sum of Coin Toss Results")
# plt.xlabel("Number of Tosses")
# plt.ylabel("y")
# plt.show()

end_time = float(arrow.get().format('X'))
print(end_time - start_time)