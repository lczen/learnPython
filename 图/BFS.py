graph = {
    "A": ["B","C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}
def BFS(graph, s):#graph图，s为初始节点
    queue = []#队列，先进先出。先放进去再弹出来
    queue.append(s)
    visited = set()#空集合，利用集合的唯一性质，遍历过的节点都存储其中
    visited.add(s)
    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]#bfs取出节点对应的邻接节点
        for w in nodes:
            if w not in visited:
                queue.append(w)
                visited.add(w)
        print(vertex)

#求某一点到根节点距离
def bfs2(graph, s):
    queue = []
    visited = set()
    queue.append(s)
    visited.add(s)
    parent = {s : None}
    while len(queue)>0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                parent[node] = vertex
        #print(vertex)
    return parent
parent = bfs2(graph, "E")
v = 'B'
while v != None:
    print(v)
    v = parent[v]

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
#DFS(graph, "A")
