import heapq
import math

graph = {
    1: {2: 3, 3: 1, 4: 2},
    2: {1: 3, 5: 1},
    3: {1: 1},
    4: {1: 2},
    5: {2: 1}
}

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s : None}
    distance = init_distance(graph, s)

    while len(pqueue)>0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent, distance
parent, distance = dijkstra(graph, 1)
dis = 0
for k, v in distance.items():
    dis += v
print(dis)