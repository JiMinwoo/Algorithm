# 선택정렬
# 처리되지 않은 데이터중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
# 시간복잡도가 O(N^2)

array = list(map(int,input().split()))

print(array)

for i in range(len(array)):

    im = array.index(min(array[i::]))
    array[i],array[im] = array[im],array[i]

print(array)