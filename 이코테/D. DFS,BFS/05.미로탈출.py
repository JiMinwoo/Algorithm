from collections import deque

N, M = map(int, input().split())
maze = []

for i in range(N):
    maze.append(list(map(int,input())))

# 괴물이 있는 부분 0, 없는 부분 1

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):

    queue = deque()
    queue.append((a,b))

    while queue:
        x,y = queue.popleft()
        # 상,하,좌,우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 괴물 조우
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] += 1

bfs(0,0)
print(maze[M][N])