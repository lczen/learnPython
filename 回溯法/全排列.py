class Solution:
    def generateParenthesis(self, n: int):
        re = []
        state = ''

        def dsp(state, p, q):
            if p > q:  # 右括号多于左括号，结束
                return
            if q == 0:
                re.append(state)
            if p > 0:
                dsp(state + '(', p - 1, q)  # 消耗左括号
            if q > 0:
                dsp(state + ')', p, q - 1)  # 消耗右括号

        dsp(state, n, n)
        return re

print(Solution().generateParenthesis(2))

re = []
state = ''
def dsp(state, p, q):
    if p > q:#右括号多于左括号，结束
        return
    if q == 0:
        re.append(state)
    if p > 0:
        dsp(state+'(', p-1, q)#消耗左括号
    if q > 0:
        dsp(state+')', p, q-1)#消耗右括号
"""
前提：p,q分别代表左括号，右括号数量.
1.出现一个'('消耗一个p数量；出现一个')'消耗一个q数量
2.当p>q的时候说明消耗右括号的数量多于左括号的数量。会出现())、)这种情况.
3.当q等于零的时候说明按照正确顺序加载完毕.把正确括号加入列表.
4.1 p为消耗完，消耗p
4.2 q未消耗完，消耗q
"""

#正月点灯笼
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A
def perm(A, p, q):
    if p == q:
        res.append(A[:])
        return
    else:
        for i in range(p, q+1):
            A = swap(A, p, i)
            perm(A, p+1, q)
            A = swap(A, p, i)

A = [1, 2, 3]
res = []
perm(A, 0, 2)
print(res)
