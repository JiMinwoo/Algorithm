def solution(record):
    
    new_id = dict()
    answer = []

    for i in record:
        temp = list(map(str,i.split()))

        if temp[0] != 'Leave':
            new_id[temp[1]] = temp[2]

    for i in record:
        temp = list(map(str,i.split()))
        
        if temp[0] == 'Enter':
            answer.append((new_id[temp[1]] + "님이 들어왔습니다."))
        elif temp[0] == "Leave":
            answer.append((new_id[temp[1]] + "님이 나갔습니다."))

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 프로도입장
# 라이언입장
# 프로도퇴장
# 프로도입장