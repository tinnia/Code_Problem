# import heapq
#
# N = int(input())
# left, right = [], []
# for _ in range(N):
#     tmp = int(input())
#     if len(left) == len(right):
#         heapq.heappush(left, (-tmp, tmp))
#     else:
#         heapq.heappush(right, (tmp,tmp))
#
#     if right and left[0][1] > right[0][1]:
#         l = heapq.heappop(left)[1]
#         r = heapq.heappop(right)[1]
#         heapq.heappush(right, (l, l))
#         heapq.heappush(left, (-r, r))
#     print(left, right)