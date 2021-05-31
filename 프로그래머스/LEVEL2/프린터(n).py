def solution(priorities, location):

    while True:
        if priorities[0] == max(priorities):
            break
        temp = priorities.pop(0)
        
        if max(priorities) > temp:
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return location + 1

print(solution([5,4,3,2,1],3))