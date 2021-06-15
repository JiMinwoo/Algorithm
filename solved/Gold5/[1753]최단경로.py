import heapq
import sys

INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])

def dijkstra(start):  
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start)) 

    while q:
        cost, now = heapq.heappop(q)
        for l,c in graph[now]:
            if distance[l] > cost + c:
                distance[l] = cost + c
                heapq.heappush(q,(distance[l],l))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])