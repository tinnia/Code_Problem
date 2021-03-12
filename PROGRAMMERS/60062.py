from itertools import permutations


def solution(n, weak, dist):
    if len(weak) == 1:
        return 1

    w, d = len(weak), len(dist)
    answer = d + 1
    weak += [i + n for i in weak]

    for i in range(w):
        start = weak[i:i + w]
        for rule in permutations(dist, d):
            idx, cnt = 0, 1
            tmp = start[0] + rule[idx]
            for j in range(w):
                if start[j] > tmp:
                    cnt += 1
                    if cnt > len(rule):
                        break
                    idx += 1
                    tmp = start[j] + rule[idx]
            answer = min(answer, cnt)

    if answer > d:
        return -1
    return answer


print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))
print(solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7]))
print(solution(200,	[0, 100],	[1,1])) #2
print(solution(12,	[10, 0],	[1,2])) #1
print(solution(200,	[0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])) #3
print(solution(50,	[1], [6])) #1
print(solution(30, [0, 3, 11, 21], [10, 4])) #2
