from functools import reduce
def fab(n):
    a,b = 2,3
    list_a = [2]
    # list_b = [3]
    c,d = 1,2
    list_c = [1]
    # list_d = [2]
    for i in range(n-1):
        a,b = b,a+b
        list_a.append(a)
        c,d = d,c+d
        list_c.append(c)
    sum = []
    sum_ = lambda arg1, arg2: arg1 + arg2;
    for i in range(len(list_a)):
        #print('%d/%d'%(list_a[i],list_c[i]))
        sum.append(list_a[i]/list_c[i])
    return reduce(sum_,sum)
print("该数列的前30项和: ",fab(30))

