import random as r
def sort2part():
    # 用random生成20个随机数并完成本题要求
    #your code here
    s = []
    for i in range(20):
        s.append(r.randint(0,100))
    print(s)
    a = s[0:10]
    a.sort()
    b = s[10:20]
    b.sort(reverse=True)
    s = a + b
    print(s)
    return

sort2part()