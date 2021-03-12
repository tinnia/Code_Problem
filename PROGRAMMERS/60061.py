def check(x, y, a, answer):
    # 기둥
    if a == 0:
        if [x - 1, y, 1] in answer or y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer:
            return True
        else:
            return False
    else:
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
            return True
        else:
            return False


def del_check(answer):
    for x, y, a in answer:
        if not check(x, y, a, answer):
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            if check(x, y, a, answer):
                answer.append([x, y, a])
        # 삭제
        else:
            answer.remove([x, y, a])
            if not del_check(answer):
                answer.append([x, y, a])

    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
