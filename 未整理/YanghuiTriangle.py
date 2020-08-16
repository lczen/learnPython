n = int(input('请输入三角形高度：'))

layer = 1
values = [1]

while layer <= n:
    new_values = [1]

    index = 0
    while index < len(values):
        print('%d ' % values[index], end='')
        if index < len(values) - 1:
            new_values.append(values[index] + values[index + 1])
        index += 1
    new_values.append(1)
    values = new_values
    print('')
    layer += 1
