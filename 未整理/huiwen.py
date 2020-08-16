# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s2 = []
#         s3 = []
#         for item in s:
#             if item.isdigit():
#                 s2.append(item)
#             elif item.isalpha():
#                 s2.append(item.lower())
#         s3 = list(reversed(s2))
#         print(s3)
#         print(s2)
#         if s3 == s2:
#             return True
#         else:
#             return False
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         print(filter(str.isalnum, s.lower()))
#         s = ''.join(filter(str.isalnum, s.lower()))
#         print(s)
#         return s == s[::-1]
import re
class Solution:
    def isPalindrome(self, s: str):
        pattern = re.compile(r'\w')
        s = pattern.findall(s.lower())
        return s == s[::-1]
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))