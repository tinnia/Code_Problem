N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = []


def func(x):
    if x > N:
        return
    ans.append(x)
    for i in lst:
        func(10 * x + i)


func(0)
print(max(ans))
