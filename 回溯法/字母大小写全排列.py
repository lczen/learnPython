"""
停止条件：len(temp)==len(s)
dfs回溯，从l=0开始，当是数字时候，i+1继续搜索，当是大写字母，要搜索本身和其小写，当是小写字母，要搜索本身和其大写。
时间复杂度和空间复杂度O(2^N∗N)
"""
class Solution:
    def AllSortString(self,s):
        ans = []
        pre = []
        def dfs(s, pre):
            if not s:
                return ans.append("".join(pre))
            if s[0].isalpha():
                dfs(s[1:], pre + [s[0].upper()])
                dfs(s[1:], pre + [s[0].lower()])
            else:
                dfs(s[1:], pre + [s[0]])
        dfs(s, pre)


