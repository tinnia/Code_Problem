N = int(input())
lst = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
lst.sort()
for i in card:
    st, ed = 0, N - 1
    while st <= ed:
        mid = (st + ed) // 2
        if i == lst[mid]:
            print(1, end=' ')
            break
        elif i > lst[mid]:
            st = mid + 1
        else:
            ed = mid - 1
    else:
        print(0, end=' ')