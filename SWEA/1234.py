for T in range(1, 11):
    N, nums = input().split()

    stack = []
    for num in nums:
        if not stack:
            stack.append(num)
        else:
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)
    print('#{}'.format(T), ''.join(stack))