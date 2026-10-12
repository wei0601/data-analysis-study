"""
本课学习 4 个函数：np.concatenate()、np.vstack()、np.hstack()、np.split()。
"""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))
#把两个数组合并起来。注意：拼接的数组要放在一个元组中，即 (a, b)。
a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])

print(np.vstack((a1, b1)))
#把两个数竖着拼接起来。注意：拼接的数组要放在一个元组中，即 (a, b)。纵向堆叠。
print(np.hstack((a1, b1)))
#把两个数横着拼接起来。注意：拼接的数组要放在一个元组中，即 (a, b)。横向堆叠。
#对于一维数组，hstack() 和 concatenate() 的效果相同。
#如果是二维数组，横向拼接会把列接在一起：
c = np.array([10, 20, 30, 40, 50, 60])

print(np.split(c, 3))
#把一个数组平均分成 3 个部分。
d = np.array([10, 20, 30, 40, 50, 60])

print(np.split(d, [2, 4]))
#把一个数组平均分成 3 个部分，但是指定了分割点。