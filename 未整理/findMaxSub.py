class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is '':
            return 0
        if len(s) == 0:
            return 1

        def find_max_left(s, i):
            sub_s = s[i]
            j = i - 1
            while j >= 0 and s[j] not in sub_s:
                sub_s += s[j]
                j -= 1
            return len(sub_s)
        max_length = 0
        for i in range(0,len(s)):
            max_length = max(max_length, find_max_left(i, s))
        return max_length
