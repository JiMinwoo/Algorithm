from itertools import permutations,combinations
def solution(orders, course):
    
    answer = []
    hubo = dict()

    while course:

        num = course.pop()

        for i in orders:

            temp = list(combinations(i,num))

            for j in temp:
                new_c = ''.join(sorted(j))

                if new_c not in hubo:
                    hubo[new_c] = 1
                else:
                    hubo[new_c] += 1
            
        for m in hubo:
            if max(hubo.values()) == hubo[m] and hubo[m] >= 2:
                answer.append(m)

        hubo.clear()

    return sorted(answer)