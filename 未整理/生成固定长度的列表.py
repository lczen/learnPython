import random as r
num = int(input('请用户输入一个整数：'))

list_num = [0] * num

i = 0
while(i<num):
    a = r.randint(0,1000)
    if a % 2 == 1:
        list_num[i] = a
        i += 1

print(list_num)
