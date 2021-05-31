def solution(s):
    answer = 0
    
    for _ in range(len(s)):
    
        s = s[-1] + s[:-1]
    
        checkBox = []
        ans = True

        for w in s:

            if w == "(" or w == "{" or w =="[":
                checkBox.append(w)

            elif w == ")":
                if len(checkBox) == 0:
                    ans = False
                    break
                if checkBox[-1] == "(":
                    checkBox.pop()
                else:
                    ans = False
                    break
            elif w == "}":
                if len(checkBox) == 0:
                    ans = False
                    break
                if checkBox[-1] == "{":
                    checkBox.pop()
                else:
                    ans = False
                    break
            elif w == "]":
                if len(checkBox) == 0:
                    ans = False
                    break
                if checkBox[-1] == "[":
                    checkBox.pop()
                else:
                    ans = False
                    break

        if ans and not checkBox:
            answer += 1   

    return answer

print(solution("{{{"))