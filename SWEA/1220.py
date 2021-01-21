for T in range(1, 11):
    length = int(input())
    table = [list(input().split()) for _ in range(length)]
    ans = 0
    for r in range(length):
        stack = []
        for c in range(length):
            if table[r][c] == 1 and not stack:
                stack.append(table[r][c])
            if table[r][c] == 2 and stack:
                ans += 1
                stack = []

    print('#{} {}'.format(T, ans))