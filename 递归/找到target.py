'''
小安是一个赛车手，现在想练习定点停车技术，需要以最少的步数达到目的地，另外他给自己定下一个规则：
1.他将公路分出多个定点
2.他开始起步的位置是0，目标定点是T
3.他的车每一次移动都保持同样的加速度，即当前位置为x，下一次移动到的定点为x+v，移动后的速度为v=2*v
4.他的车可以反向行驶，但他起始的速度v都为-1，并且在原来的位置上停留一步。
输入6，输出5
说明，6为目的地址，5位最短步数
0 1 3 7 7 6
'''
######### 山哥做法：
target, position = 0, 0
i, j = 1, -1
count, flag = 0, 1
target = int(input())
while position != target:
    if position < target:
        if flag == -1:
            count += 1
        flag = 1
        position += i
        count += 1
        i = i * 2
        j = -1

    if position > target:
        flag = -1
        if j == -1:
            count += 1
        position += j
        count += 1
        j = j * 2
        i = 1
print(count)

##########老胡动态规划
count = 0
step = 0
flag = 1
def cacu(sp, dp):
    global flag
    global step
    s = 1
    if flag == -1:
        while sp > dp:
            sp -= s
            s = 2*s
            step += 1
        flag = 1

    elif flag == 1:
        while sp < dp:
            sp += s
            s = 2*s
            step += 1
        flag = -1
    return sp

def fun(sp, dp):
    global count
    if sp == dp:
        #print('if sp == dp',sp==dp)
        #print('if sp == dp',count)
        return count
    else:
        sp = cacu(sp, dp)
        if sp != dp:
            count += 1    # 转折点
        return fun(sp, dp)

sp = 0
dp = int(input())
print(fun(sp, dp) + step)