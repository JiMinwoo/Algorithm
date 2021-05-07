from bisect import bisect_left, bisect_right

# arr은 정렬되어있는 배열이라는 가정하에
arr = [1,2,2,2,3,4,5]
print(bisect_right(arr,2)-bisect_left(arr,2))