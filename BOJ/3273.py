N = int(input())
lst = list(map(int, input().split()))
X = int(input())
lst.sort()
st, ed = 0, N - 1

answer = 0
while st < ed:
    if lst[st] + lst[ed] == X:
        answer += 1
        st += 1
        ed -= 1
    elif lst[st] + lst[ed] > X:
        ed -= 1
    else:
        st += 1
print(answer)