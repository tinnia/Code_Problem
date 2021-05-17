# from collections import deque
#
#
# def solution(n, edge):
#     route = dict()
#     for st, ed in edge:
#         route.setdefault(st, []).append(ed)
#         route.setdefault(ed, []).append(st)
#
#     visit = [-1] * (n + 1)
#     Q = deque()
#     Q.append((1, 0))  # (노드 번호, 깊이)
#     while Q:
#         idx, d = Q.popleft()
#         visit[idx] = d
#         for i in route[idx]:
#             if visit[i] == -1:
#                 visit[i] = d
#                 Q.append((i, d + 1))
#         d += 1
#     return visit.count(max(visit))

def solution(n, edge):
    route = dict()
    for st, ed in edge:
        route.setdefault(st - 1, []).append(ed - 1)
        route.setdefault(ed - 1, []).append(st - 1)
    print(route)
    stack = [0]
    visit = [0] * n
    visit[0] = 1
    while stack:
        tmp = stack.pop(0)
        for i in route[tmp]:
            if visit[i] == 0:
                stack.append(i)
                visit[i] = visit[tmp] + 1
    return visit.count(max(visit))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))