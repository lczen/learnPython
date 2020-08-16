#用户输入一个字符串和一个子串，程序会输出给定的子串在目标字符串中出现的次数。字符串遍历从左到右，而不是从右到左。 例如给定 'ABCDCDC' 和 'CDC' ，
#s = 'ABCDCDCDC'

# s = input('输入字符串')
# sub_s = input('输入子字符串')
# index = 0
# count = 0
# for i in range(len(s)+1):
#     if s.find(sub_s,index) != -1:
#         count += 1
#         index = s.find(sub_s,s.find(sub_s,index)+1)
# print(count)

s = input('请输入一个字符串：')
ss = input('请输入要查找的字串：')
num = 0  # 创建最后输出用的变量
for i in range(len(s)-len(ss)+1):
    if s[i]==ss[0]:
        if s[i:i+len(ss)]==ss:
            num += 1