def dfs(tl,x,y):
    # 방문한곳
    for i in range(4):
        # 상하좌우로 이동시켜보고
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 확인        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        # 값이 0이라면 
        if tl[nx][ny] == 1:
            tl[nx][ny] = 0 
            dfs(tl,nx,ny)

M, N, K= map(int, input().split())
tl = [[0] * M for _ in range(N)]

for i in range(K):
    y, x = map(int,input().split())
    tl[x][y] = 1

cnt = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if tl[i][j] == 1:
            tl[i][j] = 0
            cnt +=1
            dfs(tl,i,j)

print(cnt)