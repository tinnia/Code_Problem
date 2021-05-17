def combi(li, num):
    result = []
    if num == 0:
        return [[]]
    for i in range(len(li)):
        tmp = li[i]
        for c in combi(li[i + 1:], num - 1):
            result.append([tmp] + c)
    return result


while 1:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    answer = combi(lst[1:], 6)
    for ans in answer:
        print(*ans)
    print()


