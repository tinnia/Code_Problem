N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True, key=lambda x: abs(x))

negative = [i for i in lst if i < 0]
positive = [i for i in lst if i > 0]

answer = 0
for i in range(0, len(negative), M):
    answer += abs(negative[i]) * 2
for i in range(0, len(positive), M):
    answer += positive[i] * 2

print(answer - abs(lst[0]))