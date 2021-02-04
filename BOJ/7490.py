def func(n, ans):
    global answer
    if n == N:
        answer.append(ans)
        return
    func(n + 1, ans + '+' + str(n + 1))
    func(n + 1, ans + '-' + str(n + 1))
    func(n + 1, ans + ' ' + str(n + 1))


for _ in range(int(input())):
    N = int(input())
    answer = []
    func(1, "1")
    answer.sort()
    for i in answer:
        tmp = eval(i.replace(' ', ''))
        if not tmp:
            print(i)
    print()
