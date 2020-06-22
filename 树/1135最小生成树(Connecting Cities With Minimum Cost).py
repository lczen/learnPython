class Solution:
    def minimumCost(self, N, edges):
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        #kruskal
        if len(edges) < N - 1:
            return -1
        edges.sort(key=lambda a : a[2]) #按照cost进行排序
        parent = [i for i in range(N)]

        weights, e, k = 0, 0, 0 # e记录放入边的条数，k就是取边的
        while e < N - 1: # N-1条边就是最小生成树
            u, v, w = edges[k]
            k += 1
            x, y = find(u-1), find(v-1)
            if x != y:
                e += 1
                weights += w
                parent[x] = y
        return weights
if __name__ == '__main__':
    s = Solution()
    assert s.minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]) == 6
    #assert s.minimumCost(4, [[1,2,3],[3,4,4]]) == -1
    #assert s.minimumCost(5, [[1, 2, 4], [1, 3, 3], [2, 3, 8], [2, 4, 7], [3, 5, 1], [4, 5, 9]]) == 15

#克鲁斯卡尔算法，算法思想，先对边长进行排序，选取边长最小的，放入，然后判断有没有环，如果有，去掉最长的那个。
#普利姆算法，是加入点，判断点周围的最小值。
#https://www.bilibili.com/video/BV1Eb41177d1?from=search&seid=4892498656687403278