from itertools import combinations

L, C = map(int, input().split())
lst = input().split()
lst.sort()

for i in combinations(lst, L):
    cnt = 0
    for j in i:
        if j in 'aeiou':
            cnt += 1

    if 1 <= cnt <= L - 2:
        print(''.join(i))
