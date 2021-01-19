from collections import deque


def solution(n, edge):
    route = dict()
    for st, ed in edge:
        route.setdefault(st, []).append(ed)
        route.setdefault(ed, []).append(st)

    visit = [-1] * (n + 1)
    Q = deque()
    Q.append((1, 0))  # (노드 번호, 깊이)
    while Q:
        idx, d = Q.popleft()
        visit[idx] = d
        for i in route[idx]:
            if visit[i] == -1:
                visit[i] = d
                Q.append((i, d + 1))
        d += 1
    return visit.count(max(visit))