# 플로이드 워셜
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.
# 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다
# [DP 유형]
# 총 시간 복잡도는 O(N^3) [노드의 개수가 500이하]

INF = int(1e9) # 무한을 의미하는 값(10억) 설정

# 노드의 개수:n, 간선의 개수:m를 입력받기
n, m = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()