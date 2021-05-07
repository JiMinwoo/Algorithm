from collections import deque
subin, sis = map(int,input().split())

q = deque()
q.append(subin)

location = [0] * 100001

visited = [False] * 100001
visited[subin] = True

while q:
    lo = q.popleft()

    if lo == sis:
        print(location[lo])
        break

    for move in (lo-1,lo+1,lo*2):
        if 0<= move <= 100000 and not visited[move]:
            visited[move] = True
            location[move] += location[lo] + 1
            q.append(move)