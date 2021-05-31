N = int(input())
stu = []

for i in range(N): 
    [name, kor, eng, math] = map(str, input().split()) 
    
    stu.append([name, int(kor), int(eng), int(math)])

stu = sorted(stu, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for ans in stu:
    print(ans[0])