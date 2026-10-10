#元组 与list 最大区别是不能修改
numbers = (1, 2, 3, 4, 5)
#访问按照下标
print(numbers[0])  # 输出: 1
#set 最重要特点是不能重复，无序性所以没有下标
unique_numbers = {1, 2, 3, 4, 5}
#添加元素用add
unique_numbers.add(8)
print(unique_numbers)
#删除元素
unique_numbers.remove(2)#列表按照值删除也是remove
#变回列表
unique_number = list(set(unique_numbers))

