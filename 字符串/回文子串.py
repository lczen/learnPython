class Solution:
    def countSubstrings(self, s: str) -> int:

        def mid_out(l, r):  # 核心科技，从中间到两边
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:  # l和r总有一个会先到头
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0
        for i in range(0, len(s)): # 奇数
            ans += mid_out(i, i)   # 双数
        for i in range(0, len(s) - 1):
            ans += mid_out(i, i + 1)

        return ans