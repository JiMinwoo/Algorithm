def solution(n):

    nList = list(str(n)[::-1])
    answer = []

    for i in nList:
        answer.append(int(i))

    return answer

print(solution(12345))