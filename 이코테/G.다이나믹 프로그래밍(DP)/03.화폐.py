from collections import deque
INF = int(1e9)
N, M = map(int,input().split())
wal = []
dp = [INF] * (M+1)
dp[0] = 0

for i in range(N):
    wal.append(int(input()))

for w in range(N):
    for j in range(wal[w], M+1):
        if dp[j-wal[w]] != INF:
            dp[j] = min(dp[j],dp[j-wal[w]]+1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])