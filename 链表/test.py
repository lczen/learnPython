# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    def detectCycle(self, head):
        label = False
        if not head:
            return None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                label = True
                break
        if not label:
            return None
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-1)
a.next = b
b.next = c
c.next = d
d.next = b

print(Solution2().detectCycle(a).val)