s = input('请输入一个字符串')
num = input('请输入位置和需要改变字符用空格')

index = int(num[0])

new_s = list(s)
new_s[index] = num[2]

s = ''.join(new_s)
print(s)