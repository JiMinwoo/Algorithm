from collections import deque
def solution(time, r):

    answer = []
    wait = deque()
    pyo = deque()

    t = 0
    while t <= max(time):        
        for idx,i in enumerate(time):         
            if i == t:
                wait.append(idx)
                pyo.append(r[idx])
        if len(wait) == 1:
            answer.append(wait.popleft())

        for idx2,w in enumerate(wait):
            if min(pyo) == r[w]:  
                wait.pop(idx2)
        t+=1
    return answer

solution([0,3,1,0],[0,1,2,3])
# [0,1,3,0]	[0,1,2,3]	[0, 1, 3, 2]
# [7,6,8,1]	[0,1,2,3]	[3, 1, 0, 2]