# N, K = map(int, input().split())
# lst = list(map(int, input().split()))
# go = [0] + [sum(lst[:i]) for i in range(1, N + 1)]
# back = [go[-1] + sum(lst[i:]) for i in range(N)] + [go[-1]]
#
# if K > go[-1]:
#     for i in range(N + 1):
#         if back[i] <= K:
#             print(i)
#             break
# elif K == go[-1]:
#     print(N)
# else:
#     for i in range(N, -1, -1):
#         if go[i] <= K:
#             print(i + 1)
#             break

N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = flag = 1
for i in range(N):
    K -= lst[i]
    if K < 0:
        ans = i + 1
        flag = False
        break

if flag:
    for i in range(N-1, -1, -1):
        K -= lst[i]
        if K < 0:
            ans = i + 1
            break

print(ans)

