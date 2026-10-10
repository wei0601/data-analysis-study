#创建字符串
name = "weiwei"
name1 = 'weiwei'
city = "nanjing"
print(name," and ",name1)
#字符串拼接
first = "hello"
second = "world"
age = 20 
third = first + " " + second
print(third)
print("my name is " + name + ", I am " + str(age) + " years old.")
print(f"my name is {name}, I am {age} years old.")
#字符串长度
print(len(third))
#字符串切片
print(third[0:5])#index 0-4
print(third[:3])#index 0-2
print(third[:])#index 0-10
print(third[6:11])#index 6-10
#字符串方法
s = "  hello world      "
s = s.strip() #去掉首尾空格
s = s.upper() #转大写
print(s)
s = s.lower() #转小写
print(s)
s = s.replace("world","python")
print(s) #替换
print("python" in s) #判断是否包含
#字符串分割
text = "hello world python"
print(text.split()) #默认按空格分割
print(text.split(" ")) #按空格分割