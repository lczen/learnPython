class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        chuan = []
        maxn = 0
        for c in s:
            if not c in chuan:
                chuan.append(c)
            else:
                while chuan.pop(0) != c:
                    continue
                chuan.append(c)
            if maxn < len(chuan):
                maxn = len(chuan)
        return maxn