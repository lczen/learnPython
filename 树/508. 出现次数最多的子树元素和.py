# https://leetcode-cn.com/problems/most-frequent-subtree-sum/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        def mode(pool):

            max = 0
            res = []
            for k, v in pool.items():
                if max == v:
                    res.append(k)
                elif max < v:
                    res = [k]
                    max = v
                else:
                    continue
            return res

        def recursive(root):
            if not root:
                return 0
            l = recursive(root.left)
            r = recursive(root.right)
            val = l + r + root.val
            pool[val] = pool.get(val, 0) + 1
            return val

        pool = {}
        recursive(root)
        return mode(pool)
