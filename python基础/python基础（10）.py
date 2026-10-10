#函数进阶：参数怎么传，变量在哪里生效
#位置参数
def minus(a,b):
    return a - b 
print(minus(10,4))
print(minus(4,10))
#关键字参数 明确指定，可以改变顺序
print(minus(b=10,a=4))
print(minus(a=10,b=4))
#默认参数，无需传参
#*args不知道多少参数,把多个参数收集成一个tuple
def add(*args):
    print(*args)
add(1,2,3,4,5)
#**kwargs,把多个参数收集成一个dict
def add(**kwargs):
    print(kwargs)
add(a=1,b=2,c=3,d=4,e=5)
#变量作用域
x = 10

def test():
    x = 20
    print(x)

test()

print(x)
def sum_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result
print(sum_numbers(1,2,3,4))
def student_info(**kwrags):
    for key , value in kwrags.items():
        print(key,value)
student_info(name='xiaoming',age=18)
def get_positive_numbers(numbers):
    positive_numbers = []
    for i in numbers:
        if i > 0:
            positive_numbers.append(i)
    return positive_numbers
print(get_positive_numbers([-1,2,-3,4,-5]))
def process_scores(scores):
    result = []
    for i in scores:
        if i >= 60:
            result.append(i+5)
        else:
            continue
    return result
print(process_scores([60,50,80,70,90,65]))