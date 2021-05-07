# input() # 한 줄의 문자열을 입력 받는 함수 
# map() # 리스트의 모든 원소에 각각 특정한 함수를 적용

# 5 , 65 90 75 34 99

n = input()
data = list(map(int, input().split()))

print(data)
print(n)

# 입력을 최대한 빠르게 받는 방법
import sys
data = sys.stdin.readline().rstrip()
print(data)

a = 1
b = 1
print(a,b) # ,를 사용하는경우 띄어쓰기로 구분
print(7, end="") # 줄바꿈 없애기 