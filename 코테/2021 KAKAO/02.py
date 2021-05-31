dx = [-1,1,0,0]
dy = [0,0,-1,1]

def sec_step(graph,fst):
    while fst:
        nx, ny = fst.pop()
        for j in range(4):
            mx = nx + dx[j]
            my = ny + dy[j]
            if mx < 0 or my < 0 or mx >= 5 or my >= 5:
                continue
            if graph[mx][my] == "P":
                return 0
    return 1

def first_step(graph,a,b):
    graph[a][b] = "O"
    fst = []
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == "X":
            continue
        if graph[nx][ny] == "O":
            fst.append((nx,ny))
        if graph[nx][ny] == "P":
            return 0
    if sec_step(graph,fst) == 0:
        return 0
    else:
        return 1

def solution(places):
    answer = []
    for pic in places:
        graph = []
        for p in pic:
            graph.append(list(p))

        for i in range(5):
            for j in range(5):
                if graph[i][j] == "P":
                    temp = first_step(graph,i,j)
                    if temp == 0:
                        break
        if temp == 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution([["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))