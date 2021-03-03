N = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(sum([sum(lst[:i]) for i in range(1, N+1)]))