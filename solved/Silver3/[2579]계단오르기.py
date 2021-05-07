def solution(N,st):

    if N == 1:
        return st[1]

    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = st[1]
    dp[2] = st[1] + st[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+st[i-1]+st[i], dp[i-2]+st[i])

    return dp[N] 

N = int(input())
st = [0]

for i in range(N):
    st.append(int(input()))

print(solution(N,st))