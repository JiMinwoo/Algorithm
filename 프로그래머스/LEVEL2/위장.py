def solution(clothes):

    answer = 1

    ot = dict()

    for i in clothes:
        if i[1] in ot:
            ot[i[1]] += 1
        else:
            ot[i[1]] = 1

    for i in ot.values():
        answer *= (i+1)

    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))