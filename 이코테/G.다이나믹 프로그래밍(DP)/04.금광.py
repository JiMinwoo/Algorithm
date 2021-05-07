n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i]= list(map(int,input().split()))

print(graph)

for w in range(1,m):
    for h in range(n):
        if h == 0:
            graph[h][w] = max(graph[h+1][w-1],graph[h][w-1])+graph[h][w]
        elif h == n-1:
            graph[h][w] = max(graph[h-1][w-1],graph[h][w-1])+graph[h][w]
        else:
            graph[h][w] = max(graph[h-1][w-1],graph[h][w-1],graph[h+1][w-1]) + graph[h][w]