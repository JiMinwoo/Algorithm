import sys
def prime_list(n):
    n = n*2
    sieve = [True] * (n+1)
    cnt = 0
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i):
                sieve[j] = False
        
    print(cnt)

    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(13))
print(prime_list(100)) 

