def solution(x):

    # dp[N] : N이 되기까지의 최소 연산 수
    dp = [30000] * 30001
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1
    i = 6

    while True:

        if i%5 == 0:
            dp[i] = min(dp[i],dp[i//5]+1)
        if i%3 == 0:
            dp[i] = min(dp[i],dp[i//3]+1)
        if i%2 == 0:
            dp[i] = min(dp[i],dp[i//2]+1)
        
        dp[i] = min(dp[i],dp[i-1]+1)
        
        if i == x:
            break

        i+=1
    
    return dp[i]

print(solution(26))