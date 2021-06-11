# 입력을 최대한 빠르게 받는 방법
import sys
data = sys.stdin.readline().rstrip()

# math : 필수적인 수학적 기능제공
# gcd : 최대공약수 , a*b // gcd : 최소공배수
import math

# itertools : 순열, 조합라이브러리
# itertools permutations : 순열, combinations : 조합, product : 중복순열
from itertools import permutations

# colections : deque, Counter 
# collections Counter : 각 원소의 등장횟수 체크
from collections import deque

# heapq : Heap 자료구조를 제공
import heapq

# bisect : 이진탐색
import bisect

# sum(array),min(array),max(array)
# eval(String) 문자열을 수학적으로 계산한 결과를 return