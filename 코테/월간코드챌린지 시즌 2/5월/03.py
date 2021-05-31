def solution(string):
    
    answer = []

    for st in string:
        for i in range(0,len(st)-2):
            if st[i:i+3] == "110":
                temp = st[:i] + st[i+3:]
                print(temp)

    return answer

solution(["1110","100111100","0111111010"])
#["1110","100111100","0111111010"]	["1101","100110110","0110110111"]

# 0111111010
# 0110111110
# 0110110111

# 110 보다 큰수는 111뿐이니까 
# 111의 인덱스가 110의 인덱스보다 작다면 한번더

# DFS같은데 어렵네