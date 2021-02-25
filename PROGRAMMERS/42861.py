def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visit = [0] * n
    visit[0] = 1
    while 0 in visit:
        for cost in costs:
            st, ed, route = cost
            if visit[st] or visit[ed]:
                if visit[st] and visit[ed]:
                    continue
                else:
                    visit[st] = visit[ed] = 1
                    answer += route
                    break
    return answer


# def solution(n, costs):
#     answer = bridge = 0
#     edges = sorted([(cost[2], cost[0], cost[1]) for cost in costs])
#     parents = [i for i in range(n)]
#
#     def find(v):
#         if parents[v] != v:
#             return find(parents[v])
#         return parents[v]
#
#     for weight, st, ed in edges:
#         if find(st) != find(ed):
#             parents[find(st)] = ed
#             bridge += 1
#             answer += weight
#         if bridge == n - 1:
#             break
#
#     return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))
