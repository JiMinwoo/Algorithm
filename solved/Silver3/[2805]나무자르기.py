n, m = map(int, input().split())
tree = list(map(int, input().split()))

left, right, ans = 0, max(tree), 0
while left <= right:

    mid = (left + right) // 2

    tr = 0

    tr = sum([i-mid for i in tree if i > mid])

    if tr >= m:
        ans = mid
        left = mid + 1
    elif tr < m:
        right = mid - 1
print(ans)