def solution(n):

    nList = list(str(n))
    nList.sort(reverse=True)

    return int(''.join(nList))

print(solution(118372))