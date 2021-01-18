def solution(numbers):
    answer = set()

    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    # return list(answer)
    # python에서 set은 해쉬셋의 형태로 자동으로 오름차순이 되지 않아 틀린 케이스가 있음.
    return sorted(list(answer))