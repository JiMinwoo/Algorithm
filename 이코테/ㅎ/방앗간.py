# 아스키코드
# ord(문자) chr(숫자)
# A 65 Z 90 a 97 z 122
print(ord('A'),chr(65))

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# permutations과 combinations의 차이
# permutations은 순서를 따짐 ex) (1,2)와 (2,1) 구분해줌
# combinations은 순서를 무시함 ex) (1,2)와 (2,1)을 같은 인자 취급함
from itertools import permutations,combinations

arr = [1,2,3,4]

print(list(permutations(arr,2)))
print(list(combinations(arr,2)))

# ''.join(배열)
# 배열의 값들을 공백없이 출력
# ★join은 문자열 배열에서만 사용 가능함
print(''.join(['1','2','3','4','5']))