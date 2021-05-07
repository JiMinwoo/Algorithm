# 해결 아이디어 DP일것 같다

n = int(input())
triangle = []

for _ in range(n):
    stair = list(map(int,input().split()))
    triangle.append(stair)

for i in range(1,n):
    triangle[i][0] += triangle[i-1][0]
    for j in range(1,i):
        triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    triangle[i][-1] += triangle[i-1][-1]

print(max(triangle[n-1]))