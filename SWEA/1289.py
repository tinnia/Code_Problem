for T in range(1, int(input()) + 1):
    memory = input()
    cnt = 0
    tmp = "0"

    for i in range(len(memory)):
        if memory[i] != tmp:
            cnt += 1
            tmp = memory[i]
    print("#{} {}".format(T, cnt))