def solution(numbers):
    answer = []
    for num in numbers:

        temp = bin(num)[2:]

        while True:

            num += 1
            temp2 = bin(num)[2:]
            cnt = 0

            if len(temp) < len(temp2):
                answer.append((num-1)+(num//2))
                break

            for n in range(0,len(temp)):
                if temp[n] != temp2[n]:
                    cnt += 1

            if cnt <= 2:
                answer.append(num)
                break

    return answer

print(solution([3,7,15,31,63]))