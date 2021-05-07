def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        print(i,num,number,collected)
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

solution("54321",3)