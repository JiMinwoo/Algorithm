import heapq
def solution(n, edge):
    
    INF = int(1e9) # 무한을 의미하는 값(10억) 설정

    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    start = 1

    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))

    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 b노드로 가는 경우가 기존에 b노드로 가는 경로보다 작은경우
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(len(distance)):
        if distance[i] == INF:
            distance[i] = 0

    print(distance)

    answer = distance.count(max(distance))

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))