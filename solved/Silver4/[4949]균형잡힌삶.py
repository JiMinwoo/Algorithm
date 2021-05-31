import sys 
test = sys.stdin.readline

while True:
    line = test().rstrip()

    if line == '.': 
        break

    checkBox = []
    ans = True

    for l in line:
        if l == "(" or l =="[":
            checkBox.append(l)

        elif l == ")":
            if len(checkBox) == 0:
                ans = False
                break
            if checkBox[-1] == "(":
                checkBox.pop()
            else:
                ans = False
                break

        elif l == "]":
            if len(checkBox) == 0:
                ans = False
                break
            if checkBox[-1] == "[":
                checkBox.pop()
            else:
                ans = False
                break

    if ans and not checkBox:
        print("yes")
    else:
        print("no")