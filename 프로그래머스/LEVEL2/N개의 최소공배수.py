import math

def solution(num):
    
    num.sort()    

    lcm = num[0]

    for i in range(1,len(num)):

       lcm = num[i] * lcm // math.gcd(lcm,num[i])

    return lcm