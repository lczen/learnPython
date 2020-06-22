class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

heada = ListNode(4)
b = ListNode(1)
c = ListNode(8)
d = ListNode(4)
e = ListNode(5)
heada.next = b
b.next = c
c.next = d
d.next = e

headb = ListNode(5)
f = ListNode(0)
g = ListNode(1)

headb.next = f
f.next = g
g.next = c

print(Solution().getIntersectionNode(heada,headb).val)
