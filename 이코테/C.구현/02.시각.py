H = int(input())

cnt = 0

for i in range(H+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)

# 파이썬은 2초에 200,000 처리속도를 보장한다고 가정하고
# 24시간은 총 86400초
# 문제의 시간제약(2초)에 적합하다고 판단하고 완전탐색