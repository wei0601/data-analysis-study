"""
：缺失值处理与数据清洗基础
"""
#：NaN 是 “Not a Number” 的缩写，在数据分析中经常用来表示缺失或无效的数值。
import numpy as np

scores = np.array([80, 90, np.nan, 70, np.nan])

print(scores)
print(np.isnan(scores))#判断是否为NaN
print(np.sum(np.isnan(scores)))#统计NaN的个数
print(np.nanmean(scores))#忽略NaN，求平均值
print(np.mean(scores)) #求平均值不忽略Non
clean_scores = np.where(
    np.isnan(scores),
    0,
    scores
)

print(clean_scores)
#np.where(条件, 条件成立时的值, 条件不成立时的值)
#删除缺失值
clean_scores = scores[~np.isnan(scores)]
#~逻辑取反