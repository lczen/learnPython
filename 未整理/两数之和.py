# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def putIntoStack(list, list2, stack, stack2):
            while list:
                stack.append(list.val)
                list = list.next
            while list2:
                stack2.append(list2.val)
                list2 = list2.next
        stack = []
        stack2 = []
        putIntoStack(l1, l2, stack, stack2)
        jinwei = 0
        head = ListNode(-1)
        while stack or stack2 or jinwei:
            num = 0
            num2=0
            if stack:
                num = stack.pop()
            if stack2:
                num2 = stack2.pop()
            jinwei, mod = divmod(num+num2+jinwei,10)
            newnode = ListNode(mod)
            newnode.next = head.next
            head.next = newnode
        return head.next

#(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
head = ListNode(7)
a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
head.next = a
a.next = b
b.next = c
head2 = ListNode(5)
d = ListNode(6)
e = ListNode(4)
head2.next = d
d.next = e
head3 = Solution().addTwoNumbers(head, head2)
while head3:
    print(head3.val)
    head3 = head3.next