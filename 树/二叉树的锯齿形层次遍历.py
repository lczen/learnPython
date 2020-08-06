# Definition for a binary tree node.
# 剑指 Offer 32 - III. 从上到下打印二叉树 III
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root, ])
        while queue:
            levels.append([])
            lens = len(queue)#按层遍历这个地方必须求队列的长度
            for i in range(lens):
                node = queue.popleft()
                if level % 2 == 0:#level取余
                    levels[level].append(node.val)
                else:
                    levels[level].insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().zigzagLevelOrder(a))

def zigzag(root):
    levels = []
    if not root:
        return []
    level = 0
    queue = deque()
    queue.append(root)
    while queue:
        levels.append([])
        len_q = len(queue)##按层遍历这个地方必须求队列的长度
        for i in range(len_q):
            node = queue.popleft()
            if level % 2 == 0:##level取余
                levels[level].append(node.val)
            else:
                levels[level].insert(0,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels
print(zigzag(a))