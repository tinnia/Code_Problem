N = int(input())
lst = list(map(int, input().split()))
lst.sort()

st, ed = 0, N - 1
answer = abs(lst[st] + lst[ed])
ans_st, ans_ed = st, ed

while st < ed:
    tmp = lst[st] + lst[ed]
    if abs(tmp) < answer:
        answer = abs(tmp)
        ans_st, ans_ed = st, ed
        if answer == 0:
            break
    if tmp > 0:
        ed -= 1
    else:
        st += 1

print(lst[ans_st], lst[ans_ed])