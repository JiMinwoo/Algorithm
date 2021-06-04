N, M = map(int,input().split()) # N끊어진개수
minP = 9999999999

for _ in range(M):
    price = 0
    pack, one = map(int,input().split())
    
    if N >= 7:
        price += N//6 * pack
    if (N%6)*one > pack:
        price += pack
    else:
        price += (N*one)

    if price <= minP:
        minP = price

print(minP)