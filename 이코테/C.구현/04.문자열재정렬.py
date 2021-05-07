word = input()
answer = []
num = 0

for i in word:
    if ord(i) >= 65 and ord(i) <= 90:
        answer.append(i)
    else: 
        num += int(i)

answer.sort()
answer.append(str(num))

# ''.join(배열)
# 배열의 값들을 공백없이 출력
# join은 문자열 배열에서만 사용 가능함
print(''.join(answer))