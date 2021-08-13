def solution(a, b):
    
    yo = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    m31 = [1,3,5,7,8,10,12]
    m30 = [4,6,9,11]
    m29 = [2]

    for i in range(1,a):
        if i in m31:
            b += 31
        elif i in m30:
            b += 30
        elif i in m29:
            b += 29

    answer = yo[(b%7)-1]

    return answer
    
print(solution(1,1))