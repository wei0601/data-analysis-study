number = [10,20,30,40,50]
names = ["Alice", "Bob", "Charlie"]
data = [1, "hello", 3.14, True]
#index start with 0
print(number[0])  # Output: 10
print(number[-1])  # Output: 50
#列表可以修改 
number[0] = 100
print(number)
#修改列表的时间复杂度为 O(1) for accessing an element by index, but O(n) for inserting or deleting elements, where n is the number of elements in the list.
number.append(60)  # Add an element to the end of the list
print(number)  # Output: [100, 20, 30, 40, 50, 60]
#delete
number.remove(20)  # 按照值删除第一个匹配的元素
number.pop(2)  # 按照索引删除元素
print(number)  
#列表长度
len(number)  # Output: 4
#判断元素是否存在
print(10 in number)
#list 切片
print(number[1:4])  #按照索引
#排序
new = sorted(number)  # 升序排列，返回一个新的列表
number.sort()  # 升序排列
print(number)  # 直接修改原列表
print(new)  # 输出新的列表
