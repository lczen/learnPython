import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dis = {node: float('inf') for node in range(1, N + 1)}
        seen = [False] * (N+1)
        dis[K] = 0

        while True:
            node_index = -1
            node_value = float('inf')
            #找到最小值
            for i in range(1, N+1):
                if not seen[i] and dis[i] < node_value:
                    node_value = dis[i]
                    node_index = i
            if node_index < 0:
                break
            seen[node_index] = True
            for u, v in graph[node_index]:
                dis[u] = min(dis[u], dis[node_index]+v)
        ans = max(dis.values())
        return ans if ans < float('inf') else -1
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))