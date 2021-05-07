def solution(new_id):
    # 1단계 : 소문자 치환
    new_id = new_id.lower()
    # 2단계 : - , _ , . , 소문자 , 숫자
    # 45, 95, 46, 97(a)~122(z) , 123456789
    change_id = ""
    for i in new_id:
        temp = ord(i) # 아스키코드
        if 97 <= temp <= 122 or 48 <= temp <= 57 or temp == 45 or temp == 46 or temp == 95:
            change_id += i
    new_id = change_id
    # 3단계 : 연속 마침표 치환
    while new_id.count("..") > 0:
        new_id = new_id.replace("..",".")
    if new_id == ".":
        new_id = "aaa"
    # 4단계 : 처음과끝 마침표 제거
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    # 5단계 : 빈 문자열인경우 "a" 대입
    if len(new_id) == 0:
        new_id = "a"
    # 6단계 : 길이가 15까지
    if len(new_id) >= 16:
        new_id = new_id[:15]
    # 끝 마침표 제거
    if new_id[-1] == ".":
        new_id = new_id[:14]
    # 7단계 : 길이 2이하는 마지막 문자 길이3까지 반복
    if len(new_id) <= 2:
        while True:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break
    print(new_id)
    return new_id

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.