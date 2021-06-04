N = int(input())
card = {}

for _ in range(N):
    temp = int(input())
    if temp in card:
        card[temp] += 1
    else:
        card[temp] = 1

card = sorted(card.items(), key=lambda x: (-x[1],x[0]))
print(card[0][0])