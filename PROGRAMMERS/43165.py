def solution(numbers, target):
    answer = 0

    def func(idx, sum):
        nonlocal answer
        if idx == len(numbers)-1:
            if sum == target:
                answer += 1
            return
        func(idx+1, sum+numbers[idx])
        func(idx+1, sum-numbers[idx])

    func(-1, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
