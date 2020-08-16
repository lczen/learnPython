def test1():
    print("-------test1-1-----------")
    print(num)
    print("-------test1-2-----------")

def test2():
    try:
        print("-------test2-1-----------")
        test1()
        print("-------test2-2-----------")
    except Exception as error:
        print("捕获到了异常：",error)

    print("-------test2-3-----------")

test2()

