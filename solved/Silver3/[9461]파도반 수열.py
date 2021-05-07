K = int(input())
num = []

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(K):
    N = int(input())
    if N < 5:
        print(dp[N])
    else:
        for i in range(5,N+1):
            dp[i] = dp[i-1]+dp[i-5]
        print(dp[i])