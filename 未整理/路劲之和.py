# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum):
        ans, path = [], []

        def dfs(root, sum):
            if not root: return
            path.append(root.val)
            sum -= root.val
            #如果root是叶子节点，且root.val等于sum，把路劲加入
            if not root.left and not root.right and not sum:
                ans.append(path[:])
            dfs(root.left, sum)
            dfs(root.right, sum)
            path.pop()

        dfs(root, sum)
        return ans
a = TreeNode(2)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(4)
e = TreeNode(8)
a.left = b
a.right = c
b.left = d
b.right = e
Solution().pathSum(a,10)

ans,path= [],[]

def dfs2(root,sum):
    if not root:
        return
    path.append(root.val)
    sum -= root.val
    if not root.left and not root.right and not sum:
        ans.append(path[:])
    dfs2(root.left,sum)
    dfs2(root.right,sum)
    path.pop()