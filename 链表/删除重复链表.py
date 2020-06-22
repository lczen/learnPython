# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head
        head = p
        while p.next:
            left = p.next
            right = left
            while right.next and right.next.val == left.val:
                right = right.next
            if left == right:
                p = p.next
            else:
                p.next = right.next
        return head.next
head = ListNode(4)
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
head.next = a
a.next = b
b.next = c
print(Solution().deleteDuplicates(head).val)

