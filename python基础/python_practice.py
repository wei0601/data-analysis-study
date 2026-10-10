students = [
    {"name": "Tom", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 58},
    {"name": "Jack", "score": 76},
    {"name": "Lucy", "score": 45}
]
total = 0
for i in students:
    print(i["name"],i["score"])
    total += i["score"]
print(total/len(students))
print ([i["name"]  for i in students if i["score"] >= 60]) 
print([i["name"] for i in students if i["score"] == max([i["score"] for i in students])])
def a(s):
    total = 0
    l=len(s)
    for i in s:
        try:
            total += int(i["score"])
        except ValueError:
            l = l -1
            continue    
    return total/l
print(a(students))
students1 = [
    {"name": "Tom", "score": "85"},
    {"name": "Alice", "score": "92"},
    {"name": "Bob", "score": "abc"},
    {"name": "Jack", "score": "76"},
    {"name": "Lucy", "score": "45"}
]
print(a(students1))