# import sys
# sys.setrecursionlimit(10000)
#
# def func(idx, s):
#     global ans
#     if idx == E:
#         ans = min(ans, s)
#     if visit[idx]:
#         return
#     for i in bridge[idx]:
#         visit[idx] = 1
#         if idx == E:
#             ans = min(ans, s)
#             return
#         func(i[0], s + i[1])
#
#
# N, M = map(int, input().split())
# bridge = {}
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     if A not in bridge:
#         bridge[A] = [(B, C)]
#     else:
#         bridge[A].append((B, C))
#     if B not in bridge:
#         bridge[B] = [(A, C)]
#     else:
#         bridge[B].append((A, C))
#
# S, E = map(int, input().split())
# ans = 0xffffff
# for i in bridge[S]:
#     visit = [0] * (N + 1)
#     visit[S] = 1
#     func(i[0], i[1])
#
# print(ans)


from collections import deque


def bfs(a):
    Q = deque([S])
    visit = [0] * (N + 1)
    visit[S] = 1
    while Q:
        x = Q.popleft()
        for b, weight in bridge[x]:
            if not visit[b] and weight >= a:
                visit[b] = 1
                Q.append(b)
    return visit[E]


N, M = map(int, input().split())
bridge = [[] for _ in range(N+1)]
st = 1000000000
ed = 1

for _ in range(M):
    A, B, C = map(int, input().split())
    bridge[A].append((B, C))
    bridge[B].append((A, C))
    st = min(st, C)
    ed = max(ed, C)

S, E = map(int, input().split())

result = st
while st <= ed:
    mid = (st + ed) // 2
    if bfs(mid):
        result = mid
        st = mid + 1
    else:
        ed = mid - 1

print(result)