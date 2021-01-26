def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer


print(solution([1, 2, 3, 2, 3, 1]))
# [5, 4, 1, 2, 1, 0]
print(solution([1, 2, 3, 2, 1]))
# [4, 3, 1, 1, 0]
print(solution([3, 2, 1, 2, 3]))
# [1, 1, 2, 1, 0]
