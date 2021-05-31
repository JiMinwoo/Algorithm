import sys 

N = int(input())
test = sys.stdin.readline

stack = []

for _ in range(N):
    check = list(map(str,test().rstrip().split()))

    if check[0] == "push":
        stack.append(check[1])
    elif check[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif check[0] == "size":
        print(len(stack))
    elif check[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif check[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])