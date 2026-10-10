class student:#创建对象模板
    def __init__(self,name,age):##创建对象时自动执行的初始化过程、给对象添加属性
        self.name = name
        self.age = age
    def introduce(self):#定义功能函数
        print("我叫", self.name)
        print("我今年", self.age, "岁")