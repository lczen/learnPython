def fun(num):
    if num % 2 == 1:
        return True
    return False
l1=[1,3,6,8,10,11,17]
result = filter(fun,l1)
end = list(result)
print(end)

def f(x):
    return x * x
result = map(f,end)
print(list(result))
