# 다익스트라
# 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
# 음의 간선이 없을 때 정상적으로 동작
# 그리디알고리즘으로 분류됨

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값(10억) 설정

# 노드의 개수:n, 간선의 개수:m를 입력받기
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 최단 거리가 가장 짧은 노드의 인덱스
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    for b,c in graph[start]:
        distance[b] = c
    
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for _ in range(n-1):

        now = get_smallest_node()
        visited[now] = True # 방문처리
        
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]: # i[0] : 도착노드 i[1] : 거리
            cost = distance[now] + i[1]
            # 현재 노드를 거쳐서 b노드로 가는 경우가 기존에 b노드로 가는 경로보다 작은경우
            if distance[i[0]] > cost:
                distance[i[0]] = cost

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])