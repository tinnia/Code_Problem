def distance(hand, num):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == hand:
                tmp1 = (i, j)
            if keypad[i][j] == num:
                tmp2 = (i, j)
    return abs(tmp1[0] - tmp2[0]) + abs(tmp1[1] - tmp2[1])


def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right = i
        else:
            left_d, right_d = distance(left, i), distance(right, i)
            if left_d < right_d or (left_d == right_d and hand == 'left'):
                answer += 'L'
                left = i
            else:
                answer += 'R'
                right = i
    return answer
