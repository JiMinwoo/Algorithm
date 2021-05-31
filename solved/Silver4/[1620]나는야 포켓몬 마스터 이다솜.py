import sys 
p, q = map(int,input().split())

dogam = ["muuuuu"]

test = sys.stdin.readline

for i in range(p):
    line = test().rstrip()
    dogam.append(line)

for _ in range(q):
    qt = str(input())
    if qt.isdigit() == True:
        print(dogam[int(qt)])
    else:
        print(dogam.index(qt))