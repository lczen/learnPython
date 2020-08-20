#https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        queue = deque()

        # 获取每个课程的入度和邻节点
        for cur, pre in prerequisites:  # [1, 0]
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        # 获取所以入度为零的课程
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        # BFS
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses




