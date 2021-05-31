def solution(s):

    num = dict()

    num['zero'] = "0"
    num['one'] = "1"
    num['two'] = "2"
    num['three'] = "3"
    num['four'] = "4"
    num['five'] = "5"
    num['six'] = "6"
    num['seven'] = "7"
    num['eight'] = "8"
    num['nine'] = "9"

    for n in num.keys():
        s = s.replace(n,num[n])

    return int(s)