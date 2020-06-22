class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            #for a, b in itertools.izip(A, B):
            for i in range(len(A)):
                if A[i] != B[i]:
                    pairs.append((A[i], B[i]))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
"""
两种情况：
1.A和B完全相同的情况下，只要A中有重复的字母，那交换重复的字符，就能得到自己。
2.找A和B不同的部分，如果不同部分大于2了，那么就不行。如果正好等于2，那么把这两个不同的地方保存起来，然后做比较。
（a,b）(b,a)，颠倒以后还是(a,b)
"""