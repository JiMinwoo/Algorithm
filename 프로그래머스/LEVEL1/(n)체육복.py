def solution(n, lost, reserve):
    
    r = [x for x in reserve if x not in lost]
    l = [x for x in lost if x not in reserve]

    for i in r:
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)

    return n-len(l)

print(solution(5,[3,5],[2,4]))