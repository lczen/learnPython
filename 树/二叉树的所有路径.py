class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        from collections import deque
        if not root: return []
        res = []
        queue = deque()
        queue.appendleft([root, []])
        while queue:
            node, tmp = queue.pop()###最重要的就是这个temp，当当前节点左存在的时候，把当前节点的值记录下来。这样一直记录就能够记录到叶子节点。叶子节点左右为空。返回res
            if not node.left and not node.right:
                res.append("->".join(tmp + [str(node.val)]))
            if node.left:
                queue.appendleft([node.left, tmp + [str(node.val)]])
            if node.right:
                queue.appendleft([node.right, tmp + [str(node.val)]])
        return res
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(5)
root.left = a
root.right = b
a.right = c
print(Solution().binaryTreePaths(root))
