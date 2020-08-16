array = ['a','b','c','a','b','d']
#next =   0   0   0   1   2   0

#index =  0   1   2   3   4   5
next = [0] * len(array)
####t与i的初始位置
i = 1
t = 0

while i < len(array):
    if array[i] == array[t]:
        next[i] = t + 1
        i += 1
        t += 1
    elif t>0: #这个地方最难记，把t退回到next[t-1]位置
        t = next[t-1]
    else:#t == 0
        next[i] = 0
        i += 1

print(next)

##############
'''
一共三种情况，
1.array[i] == array[t]，next[i]=t+1
2.当array[i] != array[t],
'''
def prefix_table(pattern):
    next = [0] * len(pattern)
    ####t与i的初始位置
    i = 1
    t = 0

    while i < len(pattern):
        if pattern[i] == pattern[t]:
            next[i] = t + 1
            i += 1
            t += 1
        elif t > 0:  # 这个地方最难记，把t退回到next[t-1]位置
            t = next[t - 1]
        else:  # t == 0
            next[i] = 0
            i += 1
    return next
def move_prefix_table(prefix, n):
    for i in range(n-1, 0, -1):
        prefix[i] = prefix[i-1]
    prefix[0] = -1
    return prefix

def kmp_search(text, pattern):
    next = prefix_table(pattern)
    next = move_prefix_table(next, len(next))
    m = len(text)
    n = len(pattern)
    i = 0
    j = 0
    while i < m:
        if j == n-1 and text[i] == pattern[j]:
            print("Found at ",(i-j))
            break
            j = next[j]
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]
            if j == -1:
                i += 1
                j += 1


pattern = ['A','B','A','B','C','A','B','A','A']
text = ['A','B','A','B','A','B','C','A','B','A','A','B','A','B','A','B','A','B']
kmp_search(text, pattern)