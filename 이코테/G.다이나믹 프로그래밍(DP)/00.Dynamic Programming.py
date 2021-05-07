# 다이나믹 프로그래밍[Dynamic Programming]
# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
# 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다
# DP유형임을 파악하는 것이 중요함

# 피보나치 수열
# 재귀적 구현
# 재귀적으로 구현한 경우 이미 계산했던 문제를 다시 계산하는 비효율성을 가짐
def solution(n):

    if n == 1 or n == 2:
        return 1

    return solution(n-1) + solution(n-2)

print(solution(4))

# DP 구현
# 메모이제이션 : 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념
# 시간복잡도에서 큰 차이를 보임
dp = [0] * 100

def solution(n):

    if n == 1 or n == 2:
        return 1
    
    dp[n] = solution(n-1)+ solution(n-2)

    return dp[n]

print(solution(10))