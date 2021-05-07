from collections import deque

def bfs(jido,a,b,answer):

    road = deque()
    road.append((a,b))
    
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 0

    # 상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while road:
        x,y = road.popleft()
        
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= len(jido) or ny >= len(jido[0]):
                continue
            
            if jido[nx][ny] == 'W':
                continue

            if jido[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                road.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                answer.append(visited[i][j])

    return answer

N, M =  map(int,input().split())
maps = [list(map(str, input())) for _ in range(N)]
land = []
answer = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            bfs(maps,i,j,answer)

answer.sort()
print(answer[-1])