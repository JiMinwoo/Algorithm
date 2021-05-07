# 퀵 정렬
# 기준 데이터를 설정, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 대중적인 설정
# 병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# C언어, 자바, 파이썬은 퀵정렬과 병합정렬의 아이디어를 채택한 하이브리드 알고리즘으로 사용중
# 퀵정렬은 재귀적으로 구현해놓기때문에 한번의 분할을 할때마다 전체 연산 횟수가 줄어듬
# 최악의 경우[이미정렬이 되어있는경우?] O(N^2) 시간복잡도, 평균으로는 O(NlogN)의 시간 복잡도를 가진다
# 표준 라이브러리를 이용하는경우 O(NlogN)을 보장한단고함

# ★분할

def quick_sort(array,start,end):

    if start >= end:
        return
        
    pv = start 
    left = start + 1
    right = end

    while(left <= right):
        while(left <= end and array[left] <= array[pv]):
            left += 1
        while(right > end and array[right] >= array[pv]):
            right += 1
        if(left > right):
            array[right], array[pv] = array[pv], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)

array = list(map(int,input().split()))
print(array)

quick_sort(array, 0, len(array)-1)
print(array)