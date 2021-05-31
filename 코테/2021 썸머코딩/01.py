def solution(code, day, data):
    
    answer = []
    tm = []
    temp = dict()

    for d in data:
        price, cd, time = map(str,d.split())
        cd = cd[5:]

        if cd == code and day == time[5:-2]:
            price = int(price[6:])
            temp[time[-2:]] = price
            tm.append(time[-2:])

    tm.sort()

    for t in tm:
        answer.append(temp[t])

    return answer