a = ['1','2','3','4','5']
from collections import deque
deq = deque()
for i in a:
    deq.append(i)
for i in range(len(a)):
    print(deq.pop())

