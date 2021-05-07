cnt = 0
pt = str(input())
x, y = ord(pt[0])-96,int(pt[1])

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    
    cnt+=1

print(cnt)