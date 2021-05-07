N, M = map(int,input().split()) # 노드 , 간선
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(graph)
print(cnt)