class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root: TreeNode):
        if not root: return []
        rsv = []

        def bfs(root):
            queue = [root]
            while queue:
                nodes = []
                rsv.append(queue[-1].val)
                for node in queue:
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                queue = nodes

        bfs(root)
        return rsv
a = TreeNode('1')
b = TreeNode('2')
c = TreeNode('3')
d = TreeNode('4')
e = TreeNode('5')
f = TreeNode('6')
g = TreeNode('7')
a.left = b
a.right = c
b.left=d
b.right = e
c.left = f
c.right = g
print(Solution().rightSideView(a))
