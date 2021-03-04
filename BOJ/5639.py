import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def divide(st, ed):
    if st > ed:
        return
    root = lst[st]
    idx = st + 1
    while idx <= ed:
        if lst[idx] > root:
            break
        idx += 1

    divide(st + 1, idx - 1)
    divide(idx, ed)
    print(root)


lst = []
while 1:
    try:
        lst.append(int(input()))
    except:
        break

divide(0, len(lst) - 1)
