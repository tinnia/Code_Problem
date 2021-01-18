for T in range(1, 11):
    N = int(input())
    password = list(map(int,input().split()))
    cnt = int(input())
    cmd = list(input().split())

    for i in range(len(cmd)):
        if cmd[i] == "I":
            for j in range(int(cmd[i+2])):
                password.insert(int(cmd[i+1]) + j, int(cmd[i+j+3]))
        if cmd[i] == "D":
            for j in range(int(cmd[i+2])):
                password.remove(password[int(cmd[i+1])])
        if cmd[i] == "A":
            for j in range(int(cmd[i+1])):
                password.append(int(cmd[i+j+2]))

    print("#{}".format(T), end=" ")
    for i in range(10):
        print(password[i], end=" ")
    print()
