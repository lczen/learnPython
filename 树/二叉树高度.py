class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1