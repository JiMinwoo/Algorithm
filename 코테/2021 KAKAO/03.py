def cursorPlus(check,k,cm):
    cnt = int(cm[-1])
    while cnt > 0:
        k += 1
        if check[k] == "O":
            cnt -= 1
    return k

def cursorMinus(check,k,cm):               
    cnt = int(cm[-1])
    while cnt > 0:
        k -= 1
        if check[k] == "O":
            cnt -= 1
    return k

def solution(n, k, cmd):
    pyo = [i for i in range(n)]
    check = ["O" for _ in range(n)]
    delete = []
    cmd.reverse()

    while cmd:
        cm = cmd.pop()
        if cm[0] == "C":
            check[k] = "X"
            delete.append(k)
            if k == (n-1):
                cursorMinus(check,k,"U 1")
            else:
                cursorPlus(check,k,"D 1")
        elif cm[0] == "Z":
            check[delete.pop()] = "O"
        elif cm[0] == "D":
            k = cursorPlus(check,k,cm)
        elif cm[0] == "U":    
            k = cursorMinus(check,k,cm)
    return ''.join(check)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))