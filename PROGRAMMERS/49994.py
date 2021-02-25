def solution(dirs):
    r = c = 5
    tmp = set()
    for i in dirs:
        if i == 'U' and r - 1 >= 0:
            r -= 1
            tmp.add((r, c, r + 1, c))
        if i == 'R' and c + 1 < 11:
            c += 1
            tmp.add((r, c - 1, r, c))
        if i == 'D' and r + 1 < 11:
            r += 1
            tmp.add((r - 1, c, r, c))
        if i == 'L' and c - 1 >= 0:
            c -= 1
            tmp.add((r, c, r, c + 1))
    return len(tmp)


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
