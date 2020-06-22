###LeetCode 455.Assign Cookies
#g是需求因子，s是糖果。糖果比需求因子大的时候叫作满足。
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0 #甜品
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
g = [2, 5, 9, 9, 10, 15]
s = [1, 3, 6, 8, 20]
print(Solution().findContentChildren(g, s))