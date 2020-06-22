class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        for row in range(n-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col]+=min(triangle[row+1][col],triangle[row+1][col+1])
        return triangle[0][0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
"""
以
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
为例：

第一次对倒数第二行操作，6变成6+min(4,1)=7，5变成5+min(1,8)=6，7变成7+min(8,3)=10；这应该很好理解，当你选择的路径让你到达6时，接下来你可以选择4或者1，那么你自然会选择更小的1；当你选择的路径让你到达5时，接下来你可以选择1或者8，那么你自然会选择更小的1；当你选择的路径让你到达7时，接下来你可以选择8或者3，那么你自然会选择更小的3。

因此，可以把原来的lists变成
[
[2],
[3,4],
[7,6,10],
[4,1,8,3]
]
注意，因为我们是在原数组上进行操作，所以仍然保留了最后一行，但这不影响结果，因为我们最后会返回顶部的那个数，

继续向上操作，即操作倒数第三行，可以把lists变成
[
[2],
[9,10],
[7,6,10],
[4,1,8,3]
]

继续向上操作，即操作倒数第四行，可以把lists变成
[
[11],
[9,10],
[7,6,10],
[4,1,8,3]
]

最后，返回顶部的值。
"""
def dowtoup(arr):
    n = len(arr)
    for row in range(n-2, -1, -1):
        for col in range(len(arr[row])):
            arr[row][col] += min(arr[row+1][col], arr[row+1][col+1])
    return arr[0][0]
print(dowtoup([[2],[3,4],[6,5,7],[4,1,8,3]]))