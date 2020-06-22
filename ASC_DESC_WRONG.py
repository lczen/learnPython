def check_data(l):
    # 请完成题目要求的任务，并输出对应信息
    # your code here
    count = len(l)
    if count < 2:
        print("长度不够，短拒")
        return None
    for item in l:
        if not isinstance(item,int):
            print('不满足条件')
            return
    if sorted(l) == l:
        print('ASC')
    elif sorted(l,reverse=True) == l:
        print('DESC')
    else:
        print('WROND')

check_data([1])
check_data([1,"2"])
check_data([1,2,3,4])
check_data([4,3,2,1])
check_data([1,3,2,4])