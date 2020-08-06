# Definition for a binary tree node.
# 本题有点绕，搞一天。最后是直接手撕代码，搞的明白。
# root.right = self.recur(pre_root + i - in_left + 1, i + 1, in_right) 第一个参数的意思是：根节点索引 + 左子树长度 + 1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)
    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return 
        i = self.dic[self.po[pre_root]] 
        root = TreeNode(self.po[pre_root])
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        root.right = self.recur(pre_root + i - in_left + 1, i + 1, in_right)
        return root