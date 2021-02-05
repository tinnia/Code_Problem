for T in range(1, int(input()) + 1):
    n = int(input())
    happy = [int(input()) - 1 for _ in range(n)]
    del happy[0]
    for i in happy:
        happy = set(happy)
        happy -= set(range(i * 2, max(happy) + 1, i))
    print("#{} {}".format(T, len(happy)))
