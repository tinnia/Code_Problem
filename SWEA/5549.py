for T in range(1, int(input()) + 1):
    N = int(input())
    if N % 2:
        print('#{} Odd'.format(T))
    else:
        print('#{} Even'.format(T))