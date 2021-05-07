def solution(tickets):
    answer = []
    answer.append("ICN")

    visited = [False] * len(tickets)
    tickets.sort(key=lambda x:x[1])
    start = "ICN"

    idx = 0
    while True:

        if visited.count(True) == len(visited):
            break

        if tickets[idx][0] == start: 
            if visited[idx] == False:
                start = tickets[idx][1]            
                answer.append(start)
                visited[idx] = True
                idx = 0
        else:
            idx += 1

    return answer

print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))