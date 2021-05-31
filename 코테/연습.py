a = 2
b = 3
 
s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)
print(s) 

for i in range(2,17):
    print(format(i,'b'), end =" ")
    print(bin(i)[2:])