def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [False] * n
    visited[0] = True
    while sum(visited) != n:
        for cost in costs:
            s, e, c = cost
            if visited[s] !=  visited[e]:
                visited[s] = True
                visited[e] = True
                answer += c
                break

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))