from itertools import permutations

def solution(numbers):

    sumNum = list(permutations(numbers,2))
    answer = set()

    for i in sumNum:
        answer.add(sum(i))

    answer = [i for i in answer]
    answer.sort()

    return answer

numbers = list(map(int,input().split()))
print(solution(numbers))