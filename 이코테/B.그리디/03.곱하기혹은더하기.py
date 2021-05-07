S = input()
result = int(S[0])

for i in range(1,len(S)):
    temp = int(S[i])
    if temp<=1:
        result += temp
    else:
        result *= temp

print(result)