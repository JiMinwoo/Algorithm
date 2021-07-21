def solution(numbers, hand):
    
    answer = ''
    left = 10
    right = 12

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += "L"
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
        

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right") #LRLLLRLLRRL 