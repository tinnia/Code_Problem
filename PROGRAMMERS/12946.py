def move(one, three, two, n, answer):
    if n == 1:
        answer.append([one, three])
        return
    move(one, two, three, n - 1, answer)    # 1번 기둥 중 n - 1개를 2번 기둥으로 옮김
    answer.append([one, three])
    move(two, three, one, n - 1, answer)    # 2번 기둥 중 n - 1개를 3번 기둥으로 옮김


def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer


print(solution(2))
