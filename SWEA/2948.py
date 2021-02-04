for T in range(1, int(input())+1):
    N, M = map(int,input().split())
    lst1 = list(input().split())
    lst2 = list(input().split())
    print('#{} {}'.format(T, len(set(lst1) & set(lst2))))