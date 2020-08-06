# 平衡二叉树思想：
# 树的前序遍历。遍历节点，计算左右子树的高度，在计算同时，如果有子树不符合平衡二叉树，则返回-1，这样不需要遍历所有节点。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         self.res = True
#         def helper(root):
#             if not root:
#                 return 0
#             left = helper(root.left) + 1
#             right = helper(root.right) + 1
#             #print(right, left)
#             if abs(right - left) > 1:
#                 self.res = False
#             return max(left, right)
#         print(helper(root))
#         return self.res
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.fun(root) is not -1
    def fun(self, node):
        if not node:
            return 0
        left = self.fun(node.left)
        if left == -1:
            return -1
        right = self.fun(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1
a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
a.left = b
a.right = c
b.left = d
b.right = e
print(Solution().isBalanced(a))