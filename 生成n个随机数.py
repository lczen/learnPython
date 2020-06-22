import random as r      # 导入random库

num = int(input('请用户输入一个整数：'))  # 这里要注意input函数返回的是字符串类型，需要转成整型
l = []  # 定义一个空列表，用来装后面生成的随机数
for i in range(num):  # 循环n次
    l.append(r.random())  # 这里数字范围不限，可以用random库里不同的函数来实现
print(l)