# 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 구현난이도는 선택정렬보다는 높지만 동작속도는 빠름
# 시간복잡도 O(N^2)
# ★삽입정렬은 현재 데이터가 거의 정렬되어있는 상태라면 매우 빠르게 동작한다.

array = list(map(int,input().split()))

print(array)

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
        
print(array)

# 7 4 5 2 1
# 4 7 5 2 1
# 4 5 7 2 1 , 4 5 7 2 1
# 4 5 2 7 1 , 4 2 5 7 1 , 2 4 5 7 1