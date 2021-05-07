import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if jido[nx][ny] == 1:
                jido[nx][ny] = 0
                dfs(nx,ny)

TC = int(input())

for i in range(TC):
    M, N, K = map(int,input().split()) # 가로, 세로, 배추
    jido = [[0] * M for _ in range(N)]
    answer = 0

    for i in range(K):
        y, x = map(int,input().split())
        jido[x][y] = 1

    for i in range(N):
        for j in range(M):
            if jido[i][j] == 1:
                jido[i][j] = 0
                dfs(i,j)
                answer +=1
                
    print(answer)