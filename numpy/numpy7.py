"""
本课学习 4 个常用功能：生成随机数、设置随机种子、随机抽样、打乱数组。这些功能在统计模拟和数据分析中经常用到。
"""
import numpy as np

print(np.random.rand())       # 生成一个 0 到 1 之间的随机数
print(np.random.rand(5))      # 生成 5 个随机数
print(np.random.randint(1, 10))    # 生成 1 到 9 之间的随机整数
print(np.random.randint(1, 10, size=5))  # 生成 5 个1-9随机整数
# 设置随机种子
np.random.seed(42)#np.random.seed(42) 用来固定随机数生成过程。相同环境下重复运行这段代码，会得到相同的结果。
print(np.random.randint(1, 100, size=5))
# 随机抽样 不修改原数组
students = np.array(["Tom", "Alice", "Bob", "Lucy", "Jack"])

print(np.random.choice(students, size=3))#允许重复
print(np.random.choice(students, size=3, replace=False))#不允许重复
# 打乱数组 修改原数组
a = np.array([10, 20, 30, 40, 50])

np.random.shuffle(a) #返回值为None

print(a)