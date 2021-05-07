def solution(n):

    wm = ['수','박']
    answer = ''

    for i in range(n):
        answer += wm[i%2]
    
    return answer