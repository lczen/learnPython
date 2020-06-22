class Solution:
    def deleteDuplication(self, pHead):
        #基准指针
        pPre = None
        #慢指针
        pCur = pHead
        #快指针
        pNext = None
        while pCur != None:
            #有重复的结点
            if pCur.next != None and pCur.val == pCur.next.val:
                #赋值快指针
                pNext = pCur.next
                #让快指针移动，直至找到数值不同的节点
                while pNext.next != None and pNext.next.val == pCur.val:
                    pNext = pNext.next #退出循环的时候，pNext是最后一个的重复结点
                #如果头节点就是重复的结点，头结点也要移动
                if pCur == pHead:
                    pHead = pNext.next
                # 否则的话，基准结点要指向目前数值不一样的那个结点
                else:
                    pPre.next = pNext.next
                # 慢指针同样要移动到该位置
                pCur = pNext.next
            # 如果当前不重复，直接移动基准指针和慢指针
            else:
                pPre = pCur
                pCur = pCur.next
        return pHead
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    def deleteDuplication(self, head):
        pre = None
        cur = head
        pnext = None
        while cur != None:
            if cur.next != None and cur.val == cur.next.val:
                pnext = cur.next
                while pnext.next != None and pnext.val == pnext.next.val:
                    pnext = pnext.next
                if cur == head:
                    head = pnext.next
                else:
                    pre.next = pnext.next
                cur = pnext.next
            else:
                pre = cur
                cur = cur.next
        return head

head = ListNode(4)
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
head.next = a
a.next = b
b.next = c
#print(Solution2().deleteDuplication(head).val)


class Solution3:
    def deleteDuplication(self, head):
        pre = None
        cur = head
        pnext = None
        while cur != None:
            if cur.next != None and cur.val == cur.next.val:
                pnext = cur.next
                while pnext.next != None and pnext.val == pnext.next.val:
                    pnext = pnext.next
                if cur == head:
                    head = pnext.next
                else:
                    pre.next = pnext.next
                cur = pnext.next
            else:
                pre = cur
                cur = cur.next
        return head
print(Solution3().deleteDuplication(head).val)