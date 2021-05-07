node = int(input())
m = int(input())

graph = [[] for i in range(node+1)]
visited = [False] * (node+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
q = [1]

while q:
    node = q.pop()
    for i in graph[node]:
        if visited[i] == False:
            visited[i] = True
            q.append(i)

answer = visited.count(True)

print(answer - 1)