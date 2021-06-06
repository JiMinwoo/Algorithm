import sys
a = sys.stdin.readline

while True:
    line = a().rstrip()
    if line == "0":
        break
    else:
        print(line)