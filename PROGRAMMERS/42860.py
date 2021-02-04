def solution(name):
    names = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    answer = idx = 0
    while 1:
        answer += names[idx]
        names[idx] = 0
        if sum(names) == 0:
            break

        left = right = 1
        while names[idx - left] == 0:
            left += 1
        while names[idx + right] == 0:
            right += 1

        if left < right:
            idx, answer = idx - left, answer + left
        else:
            idx, answer = idx + right, answer + right

    return answer


print(solution("JAN"))
