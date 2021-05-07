import heapq
n, m, start = map(int,input().split())

INF = 1000000000
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

# 간선의 정보받기
# graph[a] = (b,c) 
# a노드에서 b노드로 이동하는 비용c
for i in range(m):
    st, ar, cost = map(int,input().split())
    graph[st].append((ar,cost))

# heapq : (a,b) a노드까지 이동하는 비용중 최소값 b
q = []
heapq.heappush(q,(start,0))
distance[start] = 0

while q:
    now , dist = heapq.heappop(q)
    # ★
    if distance[now] < dist:
        continue
    for i in graph[now]:
        node = i[0] # 도착노드
        e = i[1] # 도착노드까지 이동하는 비용
        if distance[node] > e + dist:
            distance[node] = e + dist
            heapq.hepapush(q,(node,e))