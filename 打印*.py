n = int(input('请输入三角形的层数：'))
for i in range(1, n + 1):
    print((n - i ) * ' ' + (2 * i - 1) * '*' + (n - i ) * ' ')
