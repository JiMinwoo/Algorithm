N = int(input())
num = list(map(int,input().split()))
dp = [0] * N
dp[0] = num[0]

for i in range(1,N):
    dp[i] = max(dp[i-1] + num[i], num[i])

print(max(dp))