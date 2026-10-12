"""
一、数组比较
二、根据条件筛选数组
三、统计符合条件的元素数量
"""
import numpy as np
a = np.array([10, 20, 30, 40])
print(a > 20)
scores = np.array([80, 55, 90, 45, 70])
result = scores[scores > 60]
print(result)

import numpy as np 
b = np.array([10, 25, 35, 50, 65, 80])
result1 = b[(b >= 30) & (b < 70)]
print(result1)

