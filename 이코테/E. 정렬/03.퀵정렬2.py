# 파이썬 리스트 슬라이싱을 이용한 간단한 퀵정렬 구현

def quick_sort(array):

    if len(array) <= 1:
        return array
    
    pv = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pv]
    right_side = [x for x in tail if x > pv]

    print(left_side)
    print(right_side)

    return quick_sort(left_side) + [pv] + quick_sort(right_side)

array = list(map(int,input().split()))
print(array)

print(quick_sort(array))