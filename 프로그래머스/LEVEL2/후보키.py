def solution(relation):
    
    answer = 0
    temp = dict()

    for i in range(len(relation[0])):
        for j in range(len(relation)):
            temp[relation[j][i]] = True
        
        if len(temp) == len(relation):
            answer += 1

    print(answer)

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])