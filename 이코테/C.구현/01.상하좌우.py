N = int(input())
x,y = 1,1
plans = list(map(str,input().split()))

# 해당 방향에 따른 좌표이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

for plan in plans:
    # 주어진 경로중 어떤방향인지 하나씩 반복문으로 체크
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 범위를 벗어나는지 여부 체크
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    # 조건을 만족한다면 좌표 이동
    x,y = nx,ny

print(x,y)