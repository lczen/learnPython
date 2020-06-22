class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        redult = 0
        m = abs(n)

        def compute(x, m):
            if m == 0:
                return 1
            if m == 1:
                return x
            temp = compute(x, m >> 1)
            temp *= temp
            if m & 1 == 1:
                temp *= x
            return temp

        if n > 0:
            return compute(x, m)
        else:
            return 1 / compute(x, m)
print(Solution().myPow(2,4))
"""
递归实现的方法类似于<斐波那契数列>
假如我们要求m的32次方.
如果我们知道了m的16次方,那么只要在这个基础上在平方就可以了.
而16次方是8次方的平方......以此类推,这样我们就需要做5次乘法:
先求平方,在平方的基础上求4次方,在4次方的基础上求8次方,在8次方的基础上求16次方,最后在16次方的基础上求32次方.
也就是如图片的递推公式:
"""