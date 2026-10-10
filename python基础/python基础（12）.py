"""
异常处理
在实际数据处理中，经常会遇到“数据有问题但程序不能直接崩掉”的情况，比如：

用户输入 "abc"，但程序要求数字
文件不存在
数据里出现空值或非法字符
除数为 0
字典里没有某个 key

这时候就需要 异常处理。
"""
#最基本方式
try:
    x = int(input("请输入一个数字："))
    print(x)
except:#处理错误
    print("输入有问题")
"""
常见异常：

ValueError 值不合法
TypeError  类型不匹配
ZeroDivisionError 除以零
KeyError 字典中不存在这个key
FileNotFoundError 文件不存在
IndexError 列表索引超出范围
IOError     输入输出错误
SyntaxError             语法错误
NameError 未定义变量    
AttributeError            对象没有这个属性
KeyboardInterrupt     用户按Ctrl+C
EOFError              用户按Ctrl+D
SystemError               Python系统错误
SystemExit               Python退出
"""
try:
    a=float(input("input two number： "))
    b=float(input("input two number："))
    print(a/b)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("请输入数字") 
score = []
with open(r"D:/code weiwei/数据分析师速成班/文件样例/score.txt","r") as file:
    for line in file:
        try:
            scoreq = int(line.strip())
            score.append(scoreq)
        except ValueError:
            continue
print(score)
try:
    with open(r"D:/code weiwei/数据分析师速成班/文件样例/score1.txt","r"):
        print("文件打开成功")
except FileNotFoundError:
    print("文件打开失败")