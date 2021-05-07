a = [0] * 7 
print(a)

a[4] = 4
print(a)

b = [1,2,3,4,5,6,7,8,9]
print(b)
print(b[::-1]) # 리스트를 반대로 출력

print(b[-1])

# 슬라이싱 List[i:j]은 List[i] ~ List[j-1] 까지의 인덱스를 가져옴
print(b[0:3])

# List Comprehension (리스트 컴프리헨션)
# 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화
c = [i for i in range(10) if i%2 == 0] 
print(c)

d = [i*i for i in range(1,9)]
print(d)

# 리스트 컴프리헨션을 이용해 2차원배열 설정
# N * M크기의 2차원배열
array = [[0] * 5 for _ in range(5)]
print(array)