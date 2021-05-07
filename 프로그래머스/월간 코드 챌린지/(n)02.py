def solution(s):

    answer = 0

    for i in range(len(s)):
        
        s = s[1:] + s[:1]

        if len(s) == 0:
            answer += 1
        
    return answer

print(solution("((("))