from collections import deque
N = int(input())
arr = deque(list(map(int,input().split())))
pl,mi,mul,div = map(int,input().split())

answer = [0,999999] # max, min

while arr:
    arr.popleft()