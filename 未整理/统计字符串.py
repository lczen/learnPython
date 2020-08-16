def str_count(s):
    # 完成对应要求的统计，并返回对应的数量
    # your code here
    #ord('a')
    list_s = list(s)
    list_s = [ord(item) for item in list_s]
    count_s = 0
    count_z = 0
    count_a = 0
    count_o = 0
    for i in list_s:
        if i == 32:
            count_s += 1
        elif 48<= i <=57:
            count_z+=1
        elif 65<= i <=90 or 97<= i <=122:
            count_a += 1
        else:
            count_o += 1
    print("空格个数：%d个" % count_s)
    print("数字个数：%d个" % count_z)
    print("英文字母个数：%d个" % count_a)
    print("其他字符个数：%d个" % count_o)  # 题目要求这里比122高的都是其它


str_count("我是xiao ming ming,今年27岁")