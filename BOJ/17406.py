# from itertools import permutations
# from copy import deepcopy
#
#
# def func(cases, arr1):
#     global ans
#     for case in cases:
#         r, c, s = case
#         r -= 1
#         c -= 1
#         for inner in range(s, 0, -1):
#             top_right = arr1[r - inner][c + inner]
#             bottom_left = arr1[r + inner][c - inner]
#             bottom_right = arr1[r + inner][c + inner]
#             for idx in range(c + inner, c - inner, -1):
#                 arr1[r - inner][idx] = arr1[r - inner][idx - 1]
#             for idx in range(r + inner, r - inner, -1):
#                 arr1[idx][c + inner] = arr1[idx - 1][c + inner]
#             for idx in range(c - inner, c + inner):
#                 arr1[r + inner][idx] = arr1[r + inner][idx + 1]
#             for idx in range(r - inner, r + inner):
#                 arr1[idx][c - inner] = arr1[idx + 1][c - inner]
#             arr1[r - inner + 1][c + inner] = top_right
#             arr1[r + inner][c + inner - 1] = bottom_right
#             arr1[r + inner - 1][c - inner] = bottom_left
#
#     for i in arr1:
#         ans = min(ans, sum(i))
#
#
# N, M, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# rules = [list(map(int, input().split())) for _ in range(K)]
# ans = 1e9
# for rule in permutations(rules, K):
#     func(rule, deepcopy(arr))
# print(ans)


# 재귀
from copy import deepcopy


def rotate(depth, r):
    if depth == K:
        # print(rotate)
        func(r)
        return
    for i in range(K):
        if visit[i] == 0:
            visit[i] = 1
            rotate(depth + 1, r + [rotates[i]])
            visit[i] = 0


def func(cases):
    global ans
    arr1 = deepcopy(arr)
    for case in cases:
        r, c, s = case
        r, c = r - 1, c - 1
        for i in range(s, 0, -1):
            top_right = arr1[r - i][c + i]
            bottom_left = arr1[r + i][c - i]
            bottom_right = arr1[r + i][c + i]
            for idx in range(c + i, c - i, -1):
                arr1[r - i][idx] = arr1[r - i][idx - 1]
            for idx in range(r + i, r - i, -1):
                arr1[idx][c + i] = arr1[idx - 1][c + i]
            for idx in range(c - i, c + i):
                arr1[r + i][idx] = arr1[r + i][idx + 1]
            for idx in range(r - i, r + i):
                arr1[idx][c - i] = arr1[idx + 1][c - i]
            arr1[r - i + 1][c + i] = top_right
            arr1[r + i][c + i - 1] = bottom_right
            arr1[r + i - 1][c - i] = bottom_left

    for i in arr1:
        ans = min(ans, sum(i))


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
rotates = [list(map(int, input().split())) for _ in range(K)]
ans = 1e9
visit = [0] * K
rotate(0, [])
print(ans)
