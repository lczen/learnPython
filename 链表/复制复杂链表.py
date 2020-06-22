# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
visited = {}
visited['a'] = 'b'
print(visited)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]#visited是字典，这里是取出数据
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
def DFS(graph, s):#graph图，s为初始节点
    stack = []#队列，先进先出。先放进去再弹出来
    stack.append(s)
    visited = set()#空集合，利用集合的唯一性质，遍历过的节点都存储其中
    visited.add(s)
    while(len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]#bfs取出节点对应的邻接节点
        for w in nodes:
            if w not in visited:
                stack.append(w)
                visited.add(w)
        print(vertex)
