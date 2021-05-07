# 재귀함수 (Recursive Function)
# 자기 자신을 다시 호출하는 함수
# 함수의 종료 조건 명시해야한다.

# 팩토리얼 구현 예제
# *참고) 수학적으로 0!, 1!의 값은 1이다.

def fac(n):
    if n<=1:
        return 1
    return fac(n-1)*n

print(fac(6))

# 유클리드 호제법(최대공약수)

def ex_gcd(a,b):

    if a%b==0:
        return b

    return ex_gcd(b,a%b)

print(ex_gcd(192,162))