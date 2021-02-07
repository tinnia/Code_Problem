def solution(arr):
    def check(r, c, n):
        if n == 1:
            if arr[r][c] == 1:
                return [0, 1]
            else:
                return [1, 0]

        l_up = check(r, c, n // 2)
        r_up = check(r, c + n // 2, n // 2)
        l_down = check(r + n // 2, c, n // 2)
        r_down = check(r + n // 2, c + n // 2, n // 2)

        if l_up == r_up == l_down == r_down == [0, 1] or l_up == r_up == l_down == r_down == [1, 0]:
            return l_up
        else:
            return list(map(sum, zip(l_up, r_up, l_down, r_down)))

    return check(0, 0, len(arr))


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
