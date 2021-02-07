def solution(s):
    lst = s.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    answer = str(min(lst)) + ' ' + str(max(lst))
    return answer


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))