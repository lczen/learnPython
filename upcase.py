# name_set1 = {'zhangsan','lisi'}
# name_set1.add('wangwu')
# print(name_set1)
#
# name_set1.update(['悟空', '八戒'])
# print(name_set1)
#
# name_set1.update(('白龙马','小燕子', '八戒'))
# print(name_set1)
#
# name_set1.update({'张飞','李逵'})
# print(name_set1)
#
# name_set1.update(['悟空', '八戒'], ['八戒','沙僧'])
# print(name_set1)
#
# name_set1.update('沙和尚')
# print(name_set1)
#
#
# print(set(range(0,5,2)))
#
# user_info = {"name":"悟空","age":100,"gender":"male","job":"取经","job":"偷桃"}
# print(user_info["job"])
#
# print(user_info.get("tel","10088"))
#
# for key in user_info.keys():
#     print("{}:{}".format(key,user_info[key]))
#
# for value in user_info.values():
#     print(value)
# for item in user_info.items():
#     print(type(item))
#     print(item)
#     print(item[0])
#     print(item[1])
#
# for key,value in user_info.items():
#     print("{}:{}".format(key,value))
#
# print(set())
# print(str([1,2,3]))
#
# s1 = 'a'
# s2 = 'b'
# d = {s1:1,s2:2}
# print(type(d))
#
# c = {'a':1,1:2}
# print(c['a'])
#
# def return_set():
#     return {2, 2, 3, 1}
# a, b, c = return_set()
# print(a, b, c)
#
# user_infos = [{'name':'zhangsan','age':30},{'name':'lisi','age':30},{'name':'wangwu','age':18}]
# user_infos.sort(key=lambda info:info['age'])#info参数表示列表内的一个字典，取字典中的年龄作为排序的key
# print(user_infos)
# user_infos.sort(key=lambda info:info['age'],reverse=True)
# print(user_infos)
#
# print('hello1')
# raise Exception('test')
# print('hello')

# try:
#     open('test.txt','r')
# except FileNotFoundError as err:
#     print('捕获到了异常',err)
# print('哈哈哈哈')
try:
    print(num)
    open('test.txt','r')
except (NameError,FileNotFoundError) as error:
    print('捕获到了异常',error)
print('哈哈哈哈')
