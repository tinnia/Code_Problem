from itertools import combinations


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


for t in range(int(input())):
    lst = list(map(int, input().split()))
    answer = 0
    for com in combinations(lst[1:], 2):
        answer += gcd(com[0], com[1])
    print(answer)
