N = int(input()) # 거스름돈 1260

money = [500,100,50,10]
cnt = 0

for i in money:
    if N > 0:
       cnt += N//i
       N = N%i 

print(cnt)