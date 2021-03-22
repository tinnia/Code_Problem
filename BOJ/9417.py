from itertools import combinations


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


for N in range(int(input())):
    lst = list(map(int, input().split()))
    answer = 1
    for com in combinations(lst, 2):
        answer = max(answer, gcd(com[0], com[1]))
    print(answer)
