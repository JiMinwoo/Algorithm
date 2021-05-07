from collections import deque
w, h = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
haru = deque()
tomato = deque()

for i in range(w):
    for j in range(h):
        if farm[j][i] == 1:
            haru.append((j,i))

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
day = 0

while haru:

    day += 1
    tomato = haru.copy()
    haru.clear()

    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if farm[nx][ny] == 0:
                farm[nx][ny] = 1
                haru.append((nx,ny))

for i in farm:
    if i.count(0) >= 1:
        day = 0
        break

print(day-1)