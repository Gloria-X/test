# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import arrow

start_time = float(arrow.get().format('X'))

x = []
y = []
last_running_sum = 0

for i in range(10):
    last_running_sum += np.random.choice([-1, 1])
    x.append(np.random.choice([-1, 1]))
    y.append(last_running_sum)

print(x)
print(y)


# 生成图像
# plt.plot(x,y)
# plt.title("Running Sum of Coin Toss Results")
# plt.xlabel("Number of Tosses")
# plt.ylabel("y")
# plt.show()

# plt y

end_time = float(arrow.get().format('X'))

print(end_time - start_time)