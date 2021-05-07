# 순차탐색과 이진탐색
# 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 이진탐색은 O(logN)의 시간복잡도를 보장함

def binary_search(array,target,start,end):

    mid = (start+end) // 2

    if target == array[mid]:
        return mid

    if array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

N, target = map(int, input().split())

array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search(array,target,0,N-1)

if result == None:
    print("Fail")
else:
    print(result+1)