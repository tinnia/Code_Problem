def check(n):
    nums = str(n)
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return -1
    return n


for T in range(1, int(input()) + 1):
    N = int(input())
    aj = list(map(int, input().split()))
    val = -1
    for i in range(len(aj) - 1):
        for j in range(i + 1, len(aj)):
            num = check(aj[i] * aj[j])
            if val < num:
                val = num
    print('#{} {}'.format(T, val))
