def solution(answers):

    tp1 = [1,2,3,4,5]
    tp2 = [2,1,2,3,2,4,2,5]
    tp3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    sc = [0,0,0]

    for i in range(0,len(answers)):
        if tp1[i%5] == answers[i]:
            sc[0] += 1
        if tp2[i%8] == answers[i]:
            sc[1] += 1
        if tp3[i%10] == answers[i]:
            sc[2] += 1

    for i in range(3):
        if sc[i] == max(sc):
            answer.append(i+1)

    return answer