def solution(n):
    F = [0,1]
    i=2

    while True:
        if i > n:
            break
        F.append(F[i-1]+F[i-2])

        i+=1

    return F[n]%1234567