def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    visited = [False] * len(routes)

    for i in range(len(routes)):
    
        if visited[i] == False:
            cam = routes[i][1]
            answer += 1

        for j in range(i+1,len(routes)):
            if routes[j][0] <= cam <= routes[j][1] and visited[j] == False:
                visited[j] = True            
    return answer
    
solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
# 2