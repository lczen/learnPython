def check_data(l):
    if len(l) < 2:
        print('您输入的列表长度小于2，请重新输入')
    else:
        check_list = list(filter(lambda x: True if isinstance(x, int) else False, l))
        if len(l) == len(check_list):
            if l == sorted(l):
                print('ASC')
            elif l == sorted(l, reverse=True):
                print('DESC')
            else:
                print('WRONG')
        else:
            print("列表中数据类型包含非整型，请重新输入")

check_data([1])
check_data([1,"2"])
check_data([1,2,3,4])
check_data([4,3,2,1])
check_data([1,3,2,4])