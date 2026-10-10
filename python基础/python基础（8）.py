#list comprehension
#基本写法
number = []
for i in range(5):
    number.append(i)
print(number)
#用列表推导式可以写成
number1 = [i for i in range(5)]
print(number1)
#列表推导式可以添加条件
number2 = [i for i in range(5) if i % 2 == 0]
print(number2)
###字符串处理
names = ['alice', 'bob', 'charlie', 'dan', 'edith'] 
result = [name.upper() for name in names]
print(result)
