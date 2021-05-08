n = 5 # 데이터 수
m = 5 # 찾고자 하는 연속된 부분합
arr = [1,2,3,2,5]

cnt = 0
itv_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while itv_sum < m and end < n:
        itv_sum += arr[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if itv_sum == m:
        cnt += 1
    
    itv_sum -= arr[start]

print(cnt)