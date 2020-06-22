# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head) :
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #首先初始化快指针和慢指针，确保快指针走的路的长度是慢指针长度的2倍
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-1)
a.next = b
b.next = c
c.next = d
d.next = b

print(Solution().detectCycle(a).val)