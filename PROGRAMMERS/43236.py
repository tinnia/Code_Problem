def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    answer = 0
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        mins = 1e9

        prev = 0  # 이전 돌
        rock_removed = 0  # 제거한 돌의 수
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                rock_removed += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]

        if rock_removed > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mins
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
