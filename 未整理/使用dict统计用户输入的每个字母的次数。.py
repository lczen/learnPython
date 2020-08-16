#使用dict统计用户输入的每个字母的次数

dict = {}
nums = input('请输入一些大写字母：')
for i in nums:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)