jan = int(input())
wine = [0]

for i in range(jan):
    wine.append(int(input()))

def sol(jan):
    if jan == 1:
        return wine[1]

    if jan == 2:
        return wine[1] + wine[2]

    dp = [0] * (jan+1)
    dp[0] = 0
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]

    for i in range(3,jan+1):
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])

    return dp[jan]

print(sol(jan))