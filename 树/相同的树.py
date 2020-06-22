class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        #1.pq都为空，返回True
        #2.pq中只有一个为空，返回False
        #3.pq的值不相同返回False
        #4.判断pq左右孩子是否相同
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
from collections import deque
class Solution2:
    def isSameTree2(self, p, q):
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True ##check如果值相同要return True
        queue = deque([(p, q),])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left)) ##添加进queue
                queue.append((p.right, q.right))
        return True #结为要return True
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
a2 = TreeNode(1)
b2 = TreeNode(2)
c2 = TreeNode(3)
a2.left = b2
a2.right = c2
#print(Solution().isSameTree(a, a2))
print(Solution2().isSameTree2(a, a2))