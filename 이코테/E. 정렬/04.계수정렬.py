# 계수정렬
# 특정한 조건에서만 사용가능하지만 매우 빠르게 동작
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용
# 데이터의 개수가 N, 최댓값이 K 일 때 최악의 경우에도 O(N+K)를 보장함
# 공간복잡도는 높음

array = list(map(int,input().split()))
print(array)

cnt = [0] * (max(array) + 1)

for i in array:
    cnt[i] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = ' ')

# 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있음
# ex) array가 [0,99999]인 경우

# 하지만 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능
# ex) 성적