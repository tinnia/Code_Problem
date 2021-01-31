for T in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    ans = 0

    st, ed = N // 2, N // 2 + 1
    for i in range(N // 2):
        ans += sum(board[i][st:ed])
        st -= 1
        ed += 1

    for i in range(N // 2, N):
        ans += sum(board[i][st:ed])
        st += 1
        ed -= 1

    print('#{} {}'.format(T, ans))
