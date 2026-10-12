# np.zeros(s) 创建一个s维的0向量
#np.zeros((m,n)) 创建一个m行n列的0矩阵
#np.ones(s) 创建一个s维的1向量
#np.ones((m,n)) 创建一个m行n列的1矩阵
#np.arange(start, stop, step) 创建一个从start到stop的step的数组注意：不包含终点
#np.linspace(start, stop, num) 创建一个从start到stop的num个等差数列的数组包含起点和终点。

import numpy as np
a = np.zeros(6)
print(a)

import numpy as np
b = np.ones((3, 2))



import numpy as np
chr = np.arange(2,12,2)


import numpy as np
ad = np.linspace(0,100,6)
print(a,b,chr,ad)