class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = []
        b = []
        if(len(A) != len(B)) or (len(A)==1):
            return False
        elif A==B and len(set(A))!=len(A):
            return True
        else:
            for i in range(len(A)):
                if A[i]!=B[i]:
                    a.append(A[i])
                    b.append(B[i])
            b.reverse()
            return len(a)==2 and a==b
print(Solution().buddyStrings("abab","abab"))
