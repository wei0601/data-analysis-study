"""
np.sort()#排序将数组中的元素按从小到大排序
print(np.sort(a)[::-1]) #排序并倒序
np.unique()#去重并默认按升序返回结果。
values, counts = np.unique(scores, return_counts=True)

print(values)
print(counts)以统计每个值出现的次数
np.where()#查找找出符合条件的元素位置。
np.where(条件, 条件成立时的值, 条件不成立时的值)#条件成立时返回第一个参数，条件不成立时返回第二个参数

"""
#请批改我的 NumPy 第6课练习，逐题指出错误并解释。
#第1题：
import numpy as np
a = np.array([30, 10, 50, 20, 40])
print(np.sort(a))
#第2题：
import numpy as np
b = np.array([3, 1, 5, 2, 4])
print(np.sort(b)[::-1])
#第3题：
import numpy as np
c = np.array([1, 2, 2, 3, 3, 3, 4])
print(np.unique(c))
values, counts = np.unique(c, return_counts=True) # 去重 返回每个元素出现的次数。
print(values)   # [1 2 3 4]
print(counts)   # [1 2 3 1]
#第4题：
import numpy as np
d = np.array([10, 30, 20, 40, 50])
print(np.where(d>25))
print(d[d > 25])
#   获取元素值
#第5题：
import numpy as np
scores = np.array([80, 55, 90, 45, 70])
print(np.where(scores < 60, 0 ,scores))

