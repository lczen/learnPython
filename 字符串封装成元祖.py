s = input('请输入一些字符串，用空格隔开：')
new_list = s.split(" ")
s_tuple = tuple(new_list)
print(s_tuple*3 + ("hello","world"))