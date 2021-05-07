# 다익스트라의 전체 시간 복잡도는 O(N^2)
# O(N)번의 선형탐색을 수행해야함
# 코딩테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 해결가능
# 10000개라면?

# 우선순위 큐(Priority Queue)
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

# 힙(heap)
# 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
# 최소 힙(값이 낮은데이터부터 추출), 최대 힙(값이 높은데이터부터 추출) 존재

# List의 삽입시간 : O(1), 삭제시간 : O(N)
# heap의 삽입시간 : O(logN), 삭제시간 : O(logN)

import heapq

# 오름차순 힙 정렬(Heap sort)
def heapsort(iter):
    
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽임
    for value in iter:
        heapq.heappush(h, value) # 최대 힙
#       heapq.heappush(h, -value) # 최소 힙
        print(h)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 최대 힙
#       result.append(-heapq.heappop(h)) # 최소 힙
    return result

heapsort([1,3,5,7,9,2,4,6,8,0])