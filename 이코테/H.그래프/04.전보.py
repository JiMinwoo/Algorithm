# 3 2 1
# 1 2 4
# 1 3 2
# 2 4 [받는도시개수, 총 소요시간]

import heapq

# 도시의 개수, 간선의 개수, 목표도시
n, m, start = map(int,input().split())
graph = [[] for i in range(n+1)]
INF = int(1e9) # 무한을 의미하는 값(10억) 설정
distance = [INF] * (n+1)
cnt = [0] * (n+1) # cnt[N] : 노드(N)이 거쳐진 수

for _ in range(m):
    # a도시에서 b도시까지 걸리는 시간 c
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):

    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                cnt[i[0]] += 1
                heapq.heappush(q,(cost,i[0]))

    return distance

print(dijkstra(start))
print(cnt)