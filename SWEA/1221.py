for T in range(1, int(input()) + 1):
    input()
    nums = input().split()

    dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for num in nums:
        dict[num] += 1

    answer = []
    for k, v in dict.items():
        answer += [k] * v

    print(f'#{T}')
    print(*answer)
