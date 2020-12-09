def test(n):
    if n == 1:
        return 1
    else:
        return n + test(n-1)
test(10)

def test2(n):
    return n and n + test(n-1)
test2(10)

def test3(n):
    return n == 1 or n + test(n-1)
test3(10)