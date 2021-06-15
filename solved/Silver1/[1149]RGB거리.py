h = int(input())
house = [list(map(int,input().split())) for _ in range(h)]

for i in range(1,h):
    house[i][0] = min(house[i-1][1],house[i-1][2])+house[i][0]
    house[i][1] = min(house[i-1][0],house[i-1][2])+house[i][1]
    house[i][2] = min(house[i-1][0],house[i-1][1])+house[i][2]

print(min(house[h-1][0],house[h-1][1],house[h-1][2]))