# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

# 정렬된 배열에서 bisect_right - bisect_left는 해당 target의 개수를 계산가능

from bisect import bisect_left,bisect_right
    
a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))