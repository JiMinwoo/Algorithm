num = int(input())

i = 2
while not num == 1:
    if num % i == 0:
        print(i)
        num = num // i
    else:
        i += 1