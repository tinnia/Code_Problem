# N = int(input())
# lst = [int(input()) for _ in range(N)]
# lst.sort()
# for i in lst:
#     print(i)

def merge_sort(arr):
    if len(arr)< 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr


N = int(input())
lst = [int(input()) for _ in range(N)]
lst = merge_sort(lst)
for i in lst:
    print(i)