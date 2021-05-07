def solution(s):
    
    mus = s
    cut = 0
    answer = 99999

    # 자르는 단위가 늘어남
    while cut <= len(mus):
        cut += 1
        s = mus
        cnt = 1
        temp = ''

        for _ in range((len(mus)//cut)):
            p = s[:cut]
            s = s[cut:]

            if p == s[:cut]:
                cnt += 1

            else:
                if cnt == 1:
                    temp += p
                else:
                    temp += str(cnt) + p    
                cnt = 1 

        if len(mus)%cut != 0:
            temp += mus[-(len(mus)%cut):]

        if len(temp) < answer:
            answer = len(temp)

    return answer

print(solution("aabbaccc"))