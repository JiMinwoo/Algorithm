def solution(s):
    
    charlist = ""

    idx = 0
    
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                charlist += i.upper()
            else :
                charlist += i.lower()
        else:
            idx = 0
            charlist += ' '
            continue

    return charlist