from collections import deque

h, w = map(int,input().split())
graph = [list(map(int,input())) for _ in range(h)]

q = deque()
q.append((0,0))

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:

    x, y = q.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue

        if graph[nx][ny] == 1:
            q.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[h-1][w-1])