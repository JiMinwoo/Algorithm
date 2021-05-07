def solution(N,ant):

    dp = [0] * 8

    # dp[N] : N번째 창고까지의 최대값
    dp[0] = 1
    dp[1] = 3

    # 1 3 1 5
    for i in range(2,len(ant)):
        if dp[i-2] + ant[i] >= dp[i-1]:
            dp[i] = dp[i-2] + ant[i]
        else:
            dp[i] = dp[i-1]

    return dp[N-1]

# N = int(input())
# ant = list(map(int,input().split()))

print(solution(4,[1,3,1,5,6,1]))