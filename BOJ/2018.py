N = int(input())
st, ed = 1, 2
tmp = ans = 1
while ed <= N:
    if tmp >= N:
        if tmp == N:
            ans += 1
        st += 1
        ed = st + 1
        tmp = st
    tmp += ed
    ed += 1
print(ans)