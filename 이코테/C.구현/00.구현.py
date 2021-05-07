# 흔히 말하는 코테에서의 구현이란 ? 
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 뜻함

# 1.알고리즘은 간단하지만 코드길이가 긴 유형
# 2.실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 3.문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 4.적절한 라이브러리를 찾아서 사용해야 하는 문제

for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end='')
    print()

# 동, 북, 서, 남
# x : 열, y : 행
dx = [0,-1,0,1]
dy = [1,0,-1,0]


# 현재위치
x, y = 2,2

for i in range(4):
    
    nx = x + dx[i]
    ny = y + dy[i]

    print(nx,ny)