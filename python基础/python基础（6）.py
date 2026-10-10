#字典 中心思想就是键值对
student = {
    "name" : "Tom",
    "age" : 20,
    "school" : "seu"
}
#修改值/添加新的键值对（直接修改）
student["score"]  =100
print(student)
#删除
student.pop("age")
print(student)
print("name" in student)
#get 
student.get("gender","unknow")
#如果没有返回unknow
print(student.keys())
print(student.values())
print(student.items())
#遍历字典 key
for key in student:
    print(key)
