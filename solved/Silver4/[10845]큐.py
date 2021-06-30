import sys 
from collections import deque
N = int(input())
test = sys.stdin.readline
que = deque()

for _ in range(N):
    check = list(map(str,test().rstrip().split()))
    if check[0] == "push":
        que.append(check[1])
    elif check[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif check[0] == "size": 
        print(len(que))
    elif check[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif check[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif check[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])