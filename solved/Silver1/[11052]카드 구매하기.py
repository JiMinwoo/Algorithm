N = int(input())
pack = [0]
pack += list(map(int,input().split()))

dp = [0] * (N+1)
dp[1] = pack[1]
dp[2] = max(pack[2], pack[1]*2)

for i in range(3, N+1):
    for j in range(1, i//2 + 1): #j와 i-j로 만드는 경우
        dp[i] = max(pack[i], dp[j] + dp[i-j])

print(dp[N])