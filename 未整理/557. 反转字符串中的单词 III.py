class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #1.首先做split,放进
        # words = s.split()
        # nwords = []
        # for word in words:
        #     nwords.append(word[::-1])
        #
        # return ' '.join(nwords)
        return ' '.join(i[::-1] for i in s.split())
print(Solution().reverseWords("abc abc"))