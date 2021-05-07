def solution(N, number):
    # dp[N] = N으로 만들수있는 수 조합
    dp = [[] for _ in range(9)]
    dp[0] = [0]
    i=0
    while True:
        i+=1
        if i==1:
            continue
        if i>8:
            return -1

        dp[i].append(int(str(N) * i))

        for k in dp[i-1]:
            if k != 0:
                dp[i].append(k//N)

            dp[i].append(k+N)
            dp[i].append(k-N)
            dp[i].append(k*N)

        if number in dp[i]:
            return i

print(solution(1,11))
print(solution(5,12))
print(solution(2,11))