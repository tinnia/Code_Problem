for _ in range(int(input())):
    left, right = [], []
    pwd = input()
    for i in pwd:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    print(''.join(left) + ''.join(reversed(right)))