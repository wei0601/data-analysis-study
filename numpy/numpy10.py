#当两个形状不同的数组进行运算时，NumPy 会尝试自动匹配它们的形状。
import numpy as np

a = np.array([10, 20, 30])

print(a + 5)
b = np.array([1])

print(a + b)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(A + b)
"""
比较两个数组的形状时，从最后一个维度开始向前比较。每一维必须满足以下任意一个条件：

两个维度相等。

/其中一个维度是 1。
"""
import numpy as np
scores=np.array([[80,70,90],[60,85,75]])
d=np.array([5,10,0])
print(scores+d)