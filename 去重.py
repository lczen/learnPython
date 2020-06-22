def remove_same(ll):
    # 完成题目要求的任务，并返回结果
    # your code here
    dic = {}
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    ll = list(dic.keys())
    ll.sort()
    return ll


lst = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 6, 8, 8, 12, 12, 12, 12, 13]

print(remove_same(lst))