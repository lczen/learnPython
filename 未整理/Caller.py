class Caller:
    # 构造方法，初始化报数者名字以及指向下个报数者的引用
    def __init__(self, name, next_caller):
        self.__name = name
        self.__next_caller = next_caller

    # 报数，并调用下一个报数者的报数方法
    def say_number(self, content):
        print('{}:{}!'.format(self.__name, content))

        if (self.__name != None):
            self.__next_caller.say_number(content + 1)


total = int(input('报数者总数：'))
start_point = int(input('开始数字：'))

# 从链尾开始反向构造报数者链
i = total - 1
next_caller = None

while i >= 0:
    caller = Caller('Num' + str(i), next_caller)
    next_caller = caller
    i-=1

# 开始报数
caller.say_number(start_point)