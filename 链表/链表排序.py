# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
        # if not head:
        #     return head
        # cur, nxt = head, head.next
        # dummy = ListNode(float('-inf'))##哑，空变量
        # dummy.next = head
        # while nxt:
        #     if nxt.val >= cur.val:
        #         cur, nxt = nxt, nxt.next
        #     else:
        #         cur.next = nxt.next
        #         pre1, pre2 = dummy, dummy.next
        #         while nxt.val > pre2.val:
        #             pre1, pre2 = pre2, pre2.next
        #         pre1.next = nxt
        #         nxt.next = pre2
        #         nxt = cur.next
        # return dummy.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur, nxt = head, head.next
        dummy = ListNode('-inf')
        dummy.next = head
        while nxt:#这里是nxt
            if nxt.val > cur.val:#这里用if
                cur, nxt = nxt, nxt.next
            else:
                pre, pre2 = dummy, dummy.next
                cur.next = nxt.next#nxt的值小于cur的值。断开cur与nxt，cur指向nxt的下一个
                while nxt.val > pre2.val:
                    pre, pre2 = pre2, pre2.next
                pre.next = nxt
                nxt.next = pre2
                nxt = cur.next#这里是cur.next
        return dummy.next

head = ListNode(4)
a = ListNode(3)
b = ListNode(2)
c = ListNode(1)
head.next = a
a.next = b
b.next = c
new_head = Solution().insertionSortList(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next


