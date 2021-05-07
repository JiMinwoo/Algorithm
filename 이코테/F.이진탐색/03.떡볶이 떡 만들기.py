# 파라메트릭 서치
# 파라메트릭서치란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
# 일반적으로 코테에서는 이진탐색으로 해결 가능
# 큰 탐색번위에서는 이진탐색을 떠올리는것이 좋음

def cut_dduk(dduk,M,start,end):
    
    mid = (start+end) // 2
    cut = sum([i-mid for i in dduk if i > mid])

    if cut == M:
        return mid
    elif cut > M:
        cut_dduk(dduk,M,mid+1,end)
    elif cut < M:
        cut_dduk(dduk,M,start,mid-1)

N, M = map(int,input().split())
dduk = list(map(int,input().split()))

print(cut_dduk(dduk,M,0,max(dduk)))