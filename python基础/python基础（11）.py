##文件读写
"""
.txt
.csv
.xlsx
.json
.mat

一 、打开文件 open 读取文件 整个文件 read() 读取一行 readline() 读取所有行并返回列表readlines()
关闭文件close()
with open("","r") as XX:  (优点，python会自动关闭文件)
二、写入文件 "w" XX.write()  会覆盖原文件
三追加内容 "a" xx.write()
四 读取文件并逐行处理
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())#去掉两侧空格
五、文件路径
同一文件夹 open("data.txt")
子文件夹 open("data/data.txt")
windows 路径 open(r"D:\data\data.txt")
"""
with open(r"D:/code weiwei/数据分析师速成班/文件样例/hello.txt","r") as file:
    content = file.read()
    print(file.read())
with open(r"D:/code weiwei/数据分析师速成班/文件样例/hello.txt","r") as file:
    for line in file:
        print(line.strip())
score=[]
with open(r"D:/code weiwei/数据分析师速成班/文件样例/score.txt","r") as file:
    for line in file:
        score.append(int(line.strip()))
print(score)
total = sum(score)
averge = total/len(score)
"""
| 文件格式       | 主要用途      | Python常用工具        |
| ---------- | --------- | ----------------- |
| `.txt`     | 普通文本      | `open()`          |
| `.csv`     | 表格数据      | `pandas`          |
| `.xlsx`    | Excel表格   | `pandas`          |
| `.json`    | 结构化数据/API | `json` / `pandas` |
| `.parquet` | 大规模数据     | `pandas`          |
| `.sql`     | 数据库数据     | `SQL` + Python    |
| `.xml`     | 结构化数据     | `xml`             |
| MATLAB文件           | Python读取方式           |
| ------------------ | -------------------- |
| `.mat` 普通文件        | `scipy.io.loadmat()` |
| 保存的是矩阵             | 通常变成 NumPy `ndarray` |
| 保存的是结构体            | 需要进一步处理              |
| MATLAB v7.3 `.mat` | 通常用 `h5py`           |

"""