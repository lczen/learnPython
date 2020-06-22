# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 利用队列实现迭代算法
        if not head:
            return None
        deq = deque()
        while head.next:
            deq.append(head)
            head = head.next
        # 此时head指向最后一个不为空的节点
        temp = head
        while deq:
            node = deq.pop()
            node.next = temp.next
            temp.next = node
            temp = node
        return head
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
print(Solution().reverseList(a))
