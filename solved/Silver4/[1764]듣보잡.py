import sys
d, b = map(int,input().split())
test = sys.stdin.readline

no_d = []
no_b = []

for _ in range(d):    
    no_d.append(test().rstrip())

for _ in range(b):
    no_b.append(test().rstrip())

ans = list(set(no_d) & set(no_b))

print(len(ans))
for a in sorted(ans):
    print(a)