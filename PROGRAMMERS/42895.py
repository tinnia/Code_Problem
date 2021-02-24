def solution(N, number):
    lst = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        tmp = [int(str(N) * i)]
        for j in range(1, i // 2 + 1):
            for x in lst[j]:
                for y in lst[i-j]:
                    tmp.append(x + y)
                    tmp.append(x - y)
                    tmp.append(y - x)
                    tmp.append(x * y)
                    if y != 0:
                        tmp.append(x // y)
                    if x != 0:
                        tmp.append(y // x)
        if number in tmp:
            return i
        lst.append(tmp)
    return -1

print(solution(5, 12))
print(solution(2, 11))