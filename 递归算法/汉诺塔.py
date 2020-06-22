def hanoi(n, A, B, C):##核心思想：A通过B到达C
    if n == 1:
        print("%s->%s"%(A, C))##如果只有一个元素，直接A move到 C
    else:
        hanoi(n-1, A, C, B)##A上面n-1个元素通过C到达B，然后把A放到C
        print("%s->%s" % (A, C))
        hanoi(n - 1, B, A, C)##B上n-1个元素通过A放到C
hanoi(3, 'A', 'B', 'C')