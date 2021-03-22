N = int(input())
lst = list(map(int, input().split()))
sum = [lst[0]]
for i in range(len(lst) - 1):
    sum.append(max(sum[i] + lst[i + 1], lst[i + 1]))
print(max(sum))