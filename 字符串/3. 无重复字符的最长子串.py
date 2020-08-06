class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxn = 0
        chuan = []
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            for i in s:
                if i not in chuan:
                    chuan.append(i)
                else:
                    while chuan.pop(0) != i: # 这里chuan并没有把最新的i放进去，所以pop的是那个重复数字i及其之前的数字
                        continue
                    chuan.append(i)
                if maxn < len(chuan):
                    maxn = len(chuan)
        return maxn
print(Solution().lengthOfLongestSubstring("abcabcbb"))

