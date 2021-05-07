from collections import deque

def bfs(a,b):
    # 상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((a,b))
    visited[a][b] = True
    cnt = 0

    while q:
        cnt += 1

        x,y = q.pop()    

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if jido[nx][ny] != 0 and visited[nx][ny] == False:
                q.append((nx,ny))
                visited[nx][ny] = True
                jido[nx][ny] = 2

    return cnt

N = int(input())
jido = [list(map(int,input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = 0
danji = []

for a in range(N):
    for b in range(N):
        if jido[a][b] == 1:
            danji.append(bfs(a,b))
            answer+=1

print(answer)
danji.sort()
for i in danji:
    print(i)