# N = int(input())
# lst1 = list(map(int, input().split()))
# M = int(input())
# lst2 = list(map(int, input().split()))
# for i in lst2:
#     if i in lst1:
#         print(1)
#     else:
#         print(0)

# 이분탐색
def binary(arr, num, st, ed):
    if st > ed:
        return 0
    m = (st + ed) // 2
    if arr[m] > num:
        return binary(arr, num, st, m -1)
    elif arr[m] < num:
        return binary(arr, num, m + 1, ed)
    else:
        return 1


N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
lst1.sort()

for i in lst2:
    print(binary(lst1, i, 0, N-1))
