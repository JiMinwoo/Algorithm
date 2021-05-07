from collections import deque
# 1 2 3 4
def bfs(graph,V):

    q = deque()
    q.append(V)
    visited = [False] * (len(graph) + 1)
    visited[V] = True

    while q:
        que = q.popleft()
        print(que, end=" ")
        for node in graph[que]:
            if visited[node] == False:
                visited[node] = True
                q.append(node)
    return

# 1 2 4 3
def dfs(graph,V,visited):

    visited[V] = True
    print(V, end=" ")
    for node in graph[V]:
        if not visited[node]:
            dfs(graph, node, visited)

    return

N, M, V = map(int,input().split()) # 노드수, 간선수, 시작지점

graph = [[] for i in range(N+1)]

for _ in range(M):

    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i = i.sort()

visited = [False] * (len(graph) + 1)
dfs(graph,V,visited)
print()
bfs(graph,V)