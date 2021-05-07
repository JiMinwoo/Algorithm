# A. STACK(선입후출)
# 파이썬에서 기본적으로 제공하는 리스트로 사용

stack = []
stack.append()
stack.pop()

# B. QUE(선입선출)

# deque(덱)라이브러리를 사용함
# 단순하게 리스트로도 기능적으로 큐를 구현할수있지만
# 시간복잡도를 고려하였을때는 deuqe라이브러를 사용
    
from collections import deque

queue = deque()

queue.append()
queue.popleft()