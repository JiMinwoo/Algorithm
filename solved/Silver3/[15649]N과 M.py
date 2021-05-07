from itertools import permutations

N,M = map(int,input().split())
temp = [i for i in range(1,N+1)]

answer = list(permutations(temp,M))

for i in answer:
    for j in i:
        print(j, end=" ")
    print()