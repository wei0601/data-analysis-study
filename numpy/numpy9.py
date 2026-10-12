"""
：矩阵乘法、转置、行列式、逆矩阵、解线性方程组。对你后面学习统计学和机器学习很有用。
"""
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])
print(A*B) #逐元素
print(A@ B)##矩阵乘法
print(A.T)  #转置
print(np.linalg.det(A))#行列式
A_inv = np.linalg.inv(A)#逆矩阵
print(A_inv)
b = np.array([5, 11])

x = np.linalg.solve(A, b)
print(x)#解线性方程组