def solution(info, query):
    answer = []
    query_li = []
    info_li = []

    for i in query:
        i = i.replace("and","")
        query_li.append(list(map(str,i.split())))
    for i in info:
        info_li.append(list(map(str,i.split())))

    while query_li:
        cnt = 0
        temp = query_li.pop(0)
        for i in info_li:
            check = True
            for j in range(4):
                if temp[j] == "-":
                    continue
                if temp[j] != i[j]:
                    check = False
                    break
            if check == True and eval(i[-1]) >= eval(temp[-1]):
                cnt+=1
        answer.append(cnt)
        
    return answer