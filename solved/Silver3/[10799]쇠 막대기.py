import sys
points = list(sys.stdin.readline().strip())
total = 0
remain = []
for i, point in enumerate(points):
    if point == ")":
        j = remain.pop()
        if i - j == 1:
            total += len(remain)
        else:
            total += 1
    else:
        remain.append(i)

print(total)
"R(((RR)(R)R))(R)"