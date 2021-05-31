test = str(input())

jms = []

for i in range(len(test)):
    jms.append(test[-i:])

jms.sort()

for j in jms:
    print(j)