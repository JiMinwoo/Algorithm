N, K = map(int,input().split())
money = []
answer = 0

for _ in range(N):
    money.append(int(input()))

while True:

    if K == 0:
        break

    m = money.pop()
    
    if K // m >= 1:
        answer += K // m
        K = K % m
    
print(answer)