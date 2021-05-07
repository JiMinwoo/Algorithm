# 크루스칼(Kruskal) 알고리즘
# 그리디 알고리즘으로 분류가능함
# 간선들을 가중치가 증가하는 순서로 정렬하고 가중치가 적은 간선이
# 사이클을 만들지 않으면 트리 간선으로 채택하는 방법
# 무방향 가중치 그래프에서 활용
# 최소 신장트리를 형성한다(최소한의 비용으로 모든 정점이 간선으로 연결되어있는것)

# 동작과정
# 그래피의 간선의 가중치를 기준으로 오름차순 정렬
# 간선을 연결했을때 노드끼리 사이클을 형성하는지 체크

# 모든 간선의 정보를 저장할 클래스. a는 한 쪽 노드, b는 다른 한 쪽 노드이며 dist는 a와 b 사이의 가중치(거리)이다.
class Edge:
    def __init__(self, a, b, dist):
        self.a = a
        self.b = b
        self.dist = dist
 
# 루트 노드를 반환하는 함수.
# 루트 노드를 구할 때 그냥 root[x]해도 되겠지만 집합 처리 개념을 사용하기 위해 함수로 따로 빼냈다.
def find_set(x):
    return root[x]
 
# 두 트리를 병합하는 함수. 일관성을 위해 노드 번호가 더 작은 것을 루트로 만든다.
def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b
 
# edges에는 [정점 a, 정점 b, a-b 사이의 거리]를 담은 Edge 객체들이 저장되어 있다.
edges = list()
edges.append(Edge(1, 7, 12))
edges.append(Edge(1, 4, 28))
edges.append(Edge(1, 2, 67))
edges.append(Edge(1, 5, 17))
edges.append(Edge(2, 4, 24))
edges.append(Edge(2, 5, 62))
edges.append(Edge(3, 5, 20))
edges.append(Edge(3, 6, 37))
edges.append(Edge(4, 7, 13))
edges.append(Edge(5, 6, 45))
edges.append(Edge(5, 7, 73))
 
n = len(edges)
root = [i for i in range(n)]  
# 모든 트리의 루트를 저장. 맨 처음에는 노드가 하나의 트리이므로 자기 자신이 루트이다.
 
total = 0  # 최단 거리
 
edges.sort(key=lambda x: x.dist)  # 우선 간선을 가중치 순으로 정렬. 가중치가 작은 순으로 순회
 
for edge in edges:  # 모든 간선에 대해서 반복한다.
    if find_set(edge.a) != find_set(edge.b):
    # 두 노드가 포함된 트리의 루트가 서로 다를 때(=두 트리를 합쳐도 사이클이 생기지 않을 때)
        union_set(edge.a, edge.b)  # 두 노드(가 포함되어 있는 트리)를 병합
        total += edge.dist
print(total)