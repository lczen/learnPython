import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}
        print(dist)
        seen = [False] * (N+1)
        print(seen)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            #找到最小且为访问的结点
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))

#时间复杂度，O(N^2)
#本算法本质上是选取未被访问的结点，如果已被访问，那么说明其周围的值都计算出来了，该中转点就不能用了。