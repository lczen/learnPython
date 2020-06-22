class Node():
    def __init__(self, data = None, next = None, pre = None):
        self.data = data # 常量
        self.next = next # Node
        self.pre = pre

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data
# [1,2,3]
# node1 = Node(data=3)
# node2 = Node(data=2, next = node1)
# node3 = Node(data=1, next = node2)

class LinkedList():
    def __init__(self, node = None):
        self.head = node
        self.tail = node
    #判断是否为空
    def isempty(self):
        return self.head == None
    # 从头部加入一个元素/结点
    def add(self, item):
        # 实例化
        tmp = Node(item)
        if self.isempty():
            self.head = tmp
        else:
            tmp.setNext(self.head)
            self.head = tmp
    #从尾部添加一个元素
    def append(self, item):
        #实例化
        tmp = Node(item)
        #尾部指针
        end = self.tail
        end.setNext(tmp)
        self.tail = tmp
    #遍历
    def travel(self):
        if not self.head:
            return self.head
        else:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
        print("\n")
    #插入
    def insert(self, index, data):
        if self.isempty():
            print("链表为空")
            return
        else:
            # 实例化
            tmp = Node(data)
            # 索引
            cur = -1
            pre_node = Node(next=self.head)
            # cur = index
            while cur<index:
                # 结点和索引同步更新
                pre_node = pre_node.next
                cur += 1
                if not pre_node:
                    print("插入的位置：{}越界".format(index))
                    return
            # 插入
            tmp.setNext(pre_node.next)
            pre_node.setNext(tmp)
    #删除
    def remove(self, index):
        if self.isempty():
            print("链表为空")
            return
        elif index == 0:
            self.head = self.head.next
        else:
            # 索引
            cur = 0
            # 前置结点
            pre = self.head
            # 想退出的是cur = index - 1
            while cur < index-1:
                # 同步更新
                cur += 1
                pre = pre.next
                # 判断是否到达尾部
                if not pre.next:
                    print("越界")
                    return
            # 删除
            pre.setNext(pre.next.next) # pre tmp = pre.next pre.next.next None!=Node tail.next = None

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    list = LinkedList(node1)
    list.add(2)
    list.add(3)
    list.append(4)
    list.travel()
    list.insert(3,5)
    list.travel()
    list.insert(10,9)
    list.remove(4)
    list.travel()