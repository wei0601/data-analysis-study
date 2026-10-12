"""
这一课学习数组的加减乘除、数组之间的运算，以及求和、平均值、最大值和最小值。这些操作以后做数据清洗和数据分析时经常用到。
"""
import numpy as np
a = np.array([10,20,30,40])
print(a + 10)
print(a - 10)
print(a * 10)
print(a / 10)
#优势 批量计算不用写循环
b = np.array([1,2,3,4])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
#这里是对应位置的元素进行运算
scores = np.array([80, 70, 90, 60, 50])
print(np.sum(scores))#求和
print(np.mean(scores))#求平均值
print(np.max(scores))#求最大值
print(np.min(scores))
#这些函数会把整个数组的元素一起计算
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(a, axis=0)) #求每一列的和
print(np.sum(a, axis=1)) #求每一行的和
