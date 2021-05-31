N, M = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0

# 청소할 곳이 있는경우 움직이는 방향
dx = [-1,0,1,0] 
dy = [0,1,0,-1]
# 전부다 벽인경우
back_x = [0,1,0,-1]
back_y = [1,0,-1,0]

print(graph[7][2])

def dfs(cnt,x,y,d):
    nx = x + dx[d%4]
    ny = y + dy[d%4]

    if nx < 0 or ny < 0 or nx >= M or ny >= N:
        dfs(cnt,x,y,d+1)
    if visited[nx][ny] == True or graph[nx][ny] == 1:
        dfs(cnt,x,y,d+1)
    if graph[nx][ny] == 0:
        visited[nx][ny] = True
        print(nx,ny)
        cnt += 1
        dfs(cnt,nx,ny,d+1) 
    if graph[x+back_x[d%4]][y+back_x[d%4]] == 0:
        print(x+back_x[d%4],y+back_x[d%4])
        dfs(cnt,x+back_x[d%4],y+back_x[d%4],d)

    return cnt

visited[c-1][r-1] = True
dfs(cnt,c-1,r-1,d)