#why we need numpy 
"""
for example we have the score of five student and we want to add ten point for each syudent.
we can do this job by using list
numpy 通常存储同一类型的数据，进行高效的批量计算 
"""
scores = [80, 70, 90, 60, 50]
new_scores = []
for score in scores:
    score += 10
    new_scores.append(score) 
print(new_scores)
# but by using numpy we can avoid write 循环语句
import numpy as np
acores = np.array([80, 70, 90, 60, 50]) 
print(acores + 10)
print(type(acores))


b = np.array([1, 2, 3,4,5])
a = [1, 2, 3, 4, 5]
print(b * 3)
print(a * 3)
#普通列表的 * 3 表示重复三次，而 NumPy 数组的 * 3 表示每个元素乘以 3。这是两者的重要区别。
#一维数组用一层列表，二维数组用外层列表包含多个内层列表
# python -m pip install numpy 安装numpy