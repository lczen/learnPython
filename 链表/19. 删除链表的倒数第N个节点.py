# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/chao-ke-ai-dong-hua-jiao-ni-ru-he-shan-chu-lian-bi/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        slow = ListNode(None)
        slow.next = head
        fast = slow
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next == head:
            head = head.next
            return head
        else:
            slow.next = slow.next.next

        return head