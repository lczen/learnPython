"""
时间复杂度：3^M*4^N(M代表三个字母的数量，N代表四个字母的数量)
"""
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        ans = []
        conbination = ""
        def backtrack(conbination, nextdigit):
            if not nextdigit:
                ans.append(conbination)
                return

            for letter in phone[nextdigit[0]]:
                backtrack(conbination + letter, nextdigit[1:])

        backtrack('', digits)
        return ans
print(Solution().letterCombinations('23'))